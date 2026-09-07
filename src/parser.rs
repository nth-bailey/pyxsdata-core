use pyo3::prelude::*;
use pyo3::types::{PyDict, PyList};
use quick_xml::events::Event;
use quick_xml::Reader;
use std::collections::HashMap;
use std::sync::Arc;

use crate::converters::ValueConverter;
use crate::schema::{ModelSchema, ScalarType, ValueType};

struct StackFrame {
    schema: Arc<ModelSchema>,
    element_name: Vec<u8>,
    scalar_values: HashMap<usize, PyObject>,
    list_values: HashMap<usize, Vec<PyObject>>,
    frame_text_buf: Vec<u8>,
}

impl StackFrame {
    fn new(schema: Arc<ModelSchema>, element_name: Vec<u8>) -> Self {
        Self {
            schema,
            element_name,
            scalar_values: HashMap::new(),
            list_values: HashMap::new(),
            frame_text_buf: Vec::new(),
        }
    }

    fn finish<'py>(&mut self, py: Python<'py>) -> PyResult<PyObject> {
        let kwargs = PyDict::new_bound(py);
        let mut post_init_fields: Vec<(usize, PyObject)> = Vec::new();

        // Populate collected fields
        for (idx, val) in &self.scalar_values {
            let field = &self.schema.fields[*idx];
            if field.is_init {
                kwargs.set_item(&field.py_name_obj, val)?;
            } else {
                post_init_fields.push((*idx, val.clone_ref(py)));
            }
        }

        for (idx, list_items) in &self.list_values {
            let field = &self.schema.fields[*idx];
            let py_list = PyList::new_bound(py, list_items);
            if field.is_init {
                kwargs.set_item(&field.py_name_obj, py_list)?;
            } else {
                post_init_fields.push((*idx, py_list.into_any().unbind()));
            }
        }

        if let Some(text_idx) = self.schema.text_field {
            if !self.frame_text_buf.is_empty() {
                let field = &self.schema.fields[text_idx];
                if let ValueType::Scalar(ref scalar_type) = field.val_type {
                    let py_val =
                        ValueConverter::parse_scalar(py, scalar_type, &self.frame_text_buf)?;
                    if field.is_init {
                        kwargs.set_item(&field.py_name_obj, py_val)?;
                    } else {
                        post_init_fields.push((text_idx, py_val.unbind()));
                    }
                }
            }
        }

        let cls = self.schema.py_class.bind(py);
        let instance = cls.call((), Some(&kwargs))?;
        for (idx, val) in post_init_fields {
            let field = &self.schema.fields[idx];
            instance.setattr(&*field.py_name, val)?;
        }
        Ok(instance.unbind())
    }
}

pub struct XmlDeserializer;

fn is_nil_element(e: &quick_xml::events::BytesStart) -> bool {
    for attr in e.attributes().flatten() {
        let key = attr.key.local_name();
        if (key.as_ref() == b"nil" || key.as_ref() == b"xsi:nil")
            && (attr.value.as_ref() == b"true" || attr.value.as_ref() == b"1")
        {
            return true;
        }
    }
    false
}

impl XmlDeserializer {
    pub fn deserialize<'py>(
        py: Python<'py>,
        xml_bytes: &[u8],
        root_schema: Arc<ModelSchema>,
    ) -> PyResult<PyObject> {
        let mut reader = Reader::from_reader(xml_bytes);
        reader.config_mut().trim_text(true);

        let mut stack: Vec<StackFrame> = Vec::with_capacity(16);
        let mut active_scalar_field: Option<(usize, ScalarType, bool)> = None;
        let mut text_buf: Vec<u8> = Vec::new();

        let mut buf = Vec::new();

        loop {
            match reader.read_event_into(&mut buf) {
                Ok(Event::Start(ref e)) => {
                    let local_name = e.local_name().as_ref().to_vec();
                    let is_nil = is_nil_element(e);

                    if stack.is_empty() {
                        // Root element
                        let mut frame = StackFrame::new(Arc::clone(&root_schema), local_name);
                        Self::parse_attributes(py, e, &mut frame)?;
                        stack.push(frame);
                    } else {
                        // Check if child belongs to current active frame
                        let current_frame = stack.last().ok_or_else(|| {
                            pyo3::exceptions::PyValueError::new_err("Invalid XML: stack is empty")
                        })?;
                        if let Some(&field_idx) = current_frame.schema.element_map.get(&local_name)
                        {
                            let field = &current_frame.schema.fields[field_idx];
                            match &field.val_type {
                                ValueType::Scalar(scalar_type) => {
                                    active_scalar_field =
                                        Some((field_idx, scalar_type.clone(), is_nil));
                                    text_buf.clear();
                                }
                                ValueType::Nested(nested_schema) => {
                                    if is_nil {
                                        active_scalar_field =
                                            Some((field_idx, ScalarType::Any, true));
                                        text_buf.clear();
                                    } else {
                                        let mut frame =
                                            StackFrame::new(Arc::clone(nested_schema), local_name);
                                        Self::parse_attributes(py, e, &mut frame)?;
                                        stack.push(frame);
                                    }
                                }
                                ValueType::List(inner) => match &**inner {
                                    ValueType::Nested(nested_schema) => {
                                        if is_nil {
                                            active_scalar_field =
                                                Some((field_idx, ScalarType::Any, true));
                                            text_buf.clear();
                                        } else {
                                            let mut frame = StackFrame::new(
                                                Arc::clone(nested_schema),
                                                local_name,
                                            );
                                            Self::parse_attributes(py, e, &mut frame)?;
                                            stack.push(frame);
                                        }
                                    }
                                    ValueType::Scalar(scalar_type) => {
                                        active_scalar_field =
                                            Some((field_idx, scalar_type.clone(), is_nil));
                                        text_buf.clear();
                                    }
                                    _ => {}
                                },
                            }
                        }
                    }
                }
                Ok(Event::Text(ref e)) => {
                    if active_scalar_field.is_some() {
                        text_buf.extend_from_slice(e.as_ref());
                    } else if let Some(current_frame) = stack.last_mut() {
                        if current_frame.schema.text_field.is_some() {
                            current_frame.frame_text_buf.extend_from_slice(e.as_ref());
                        }
                    }
                }
                Ok(Event::CData(ref e)) => {
                    if active_scalar_field.is_some() {
                        text_buf.extend_from_slice(e.as_ref());
                    } else if let Some(current_frame) = stack.last_mut() {
                        if current_frame.schema.text_field.is_some() {
                            current_frame.frame_text_buf.extend_from_slice(e.as_ref());
                        }
                    }
                }
                Ok(Event::Empty(ref e)) => {
                    let local_name = e.local_name().as_ref().to_vec();
                    let is_nil = is_nil_element(e);

                    if stack.is_empty() {
                        // Empty root
                        let mut frame = StackFrame::new(Arc::clone(&root_schema), local_name);
                        Self::parse_attributes(py, e, &mut frame)?;
                        return frame.finish(py);
                    }

                    let current_frame = stack.last_mut().ok_or_else(|| {
                        pyo3::exceptions::PyValueError::new_err("Invalid XML: stack is empty")
                    })?;
                    if let Some(&field_idx) = current_frame.schema.element_map.get(&local_name) {
                        let field = &current_frame.schema.fields[field_idx];
                        if is_nil {
                            if matches!(field.val_type, ValueType::List(_)) {
                                current_frame
                                    .list_values
                                    .entry(field_idx)
                                    .or_default()
                                    .push(py.None());
                            } else {
                                current_frame.scalar_values.insert(field_idx, py.None());
                            }
                        } else {
                            match &field.val_type {
                                ValueType::Scalar(scalar_type) => {
                                    let py_val =
                                        ValueConverter::parse_scalar(py, scalar_type, b"")?;
                                    current_frame
                                        .scalar_values
                                        .insert(field_idx, py_val.unbind());
                                }
                                ValueType::Nested(nested_schema) => {
                                    let mut frame =
                                        StackFrame::new(Arc::clone(nested_schema), local_name);
                                    Self::parse_attributes(py, e, &mut frame)?;
                                    let instance = frame.finish(py)?;
                                    current_frame.scalar_values.insert(field_idx, instance);
                                }
                                ValueType::List(inner) => match &**inner {
                                    ValueType::Scalar(scalar_type) => {
                                        let py_val =
                                            ValueConverter::parse_scalar(py, scalar_type, b"")?;
                                        current_frame
                                            .list_values
                                            .entry(field_idx)
                                            .or_default()
                                            .push(py_val.unbind());
                                    }
                                    ValueType::Nested(nested_schema) => {
                                        let mut frame =
                                            StackFrame::new(Arc::clone(nested_schema), local_name);
                                        Self::parse_attributes(py, e, &mut frame)?;
                                        let instance = frame.finish(py)?;
                                        current_frame
                                            .list_values
                                            .entry(field_idx)
                                            .or_default()
                                            .push(instance);
                                    }
                                    _ => {}
                                },
                            }
                        }
                    }
                }
                Ok(Event::End(ref e)) => {
                    let local_name_obj = e.local_name();
                    let local_name = local_name_obj.as_ref();

                    if let Some((field_idx, scalar_type, is_nil)) = active_scalar_field.take() {
                        let current_frame = stack.last_mut().ok_or_else(|| {
                            pyo3::exceptions::PyValueError::new_err(
                                "Invalid XML: stack is empty on element end",
                            )
                        })?;
                        let field = &current_frame.schema.fields[field_idx];

                        let py_val = if is_nil {
                            py.None()
                        } else {
                            ValueConverter::parse_scalar(py, &scalar_type, &text_buf)?.unbind()
                        };

                        if matches!(field.val_type, ValueType::List(_)) {
                            current_frame
                                .list_values
                                .entry(field_idx)
                                .or_default()
                                .push(py_val);
                        } else {
                            current_frame.scalar_values.insert(field_idx, py_val);
                        }
                    } else if let Some(current_frame) = stack.last() {
                        if current_frame.element_name == local_name {
                            let mut popped = stack.pop().ok_or_else(|| {
                                pyo3::exceptions::PyValueError::new_err(
                                    "Invalid XML: stack underflow",
                                )
                            })?;
                            let instance = popped.finish(py)?;

                            if let Some(parent_frame) = stack.last_mut() {
                                if let Some(&parent_field_idx) =
                                    parent_frame.schema.element_map.get(local_name)
                                {
                                    let field = &parent_frame.schema.fields[parent_field_idx];
                                    if matches!(field.val_type, ValueType::List(_)) {
                                        parent_frame
                                            .list_values
                                            .entry(parent_field_idx)
                                            .or_default()
                                            .push(instance);
                                    } else {
                                        parent_frame
                                            .scalar_values
                                            .insert(parent_field_idx, instance);
                                    }
                                }
                            } else {
                                // Stack is empty, root completed!
                                return Ok(instance);
                            }
                        }
                    }
                }

                Ok(Event::Eof) => break,
                Err(e) => {
                    return Err(pyo3::exceptions::PyValueError::new_err(format!(
                        "XML parse error at position {}: {:?}",
                        reader.buffer_position(),
                        e
                    )));
                }
                _ => {}
            }
            buf.clear();
        }

        Err(pyo3::exceptions::PyValueError::new_err(
            "XML document ended unexpectedly without root completion",
        ))
    }

    fn parse_attributes<'py>(
        py: Python<'py>,
        e: &quick_xml::events::BytesStart,
        frame: &mut StackFrame,
    ) -> PyResult<()> {
        for attr in e.attributes() {
            let attr = attr.map_err(|err| {
                pyo3::exceptions::PyValueError::new_err(format!("Invalid attribute: {:?}", err))
            })?;
            let local_name_obj = attr.key.local_name();
            let attr_name = local_name_obj.as_ref();

            if let Some(&field_idx) = frame.schema.attribute_map.get(attr_name) {
                let field = &frame.schema.fields[field_idx];
                if let ValueType::Scalar(ref scalar_type) = field.val_type {
                    let py_val = ValueConverter::parse_scalar(py, scalar_type, &attr.value)?;
                    frame.scalar_values.insert(field_idx, py_val.unbind());
                }
            }
        }
        Ok(())
    }
}

#[cfg(test)]
mod tests {
    use super::*;
    use quick_xml::events::BytesStart;

    #[test]
    fn test_is_nil_element_detection() {
        let tag = BytesStart::from_content("elem xsi:nil=\"true\"", 4);
        assert!(is_nil_element(&tag));

        let tag_one = BytesStart::from_content("elem nil=\"1\"", 4);
        assert!(is_nil_element(&tag_one));

        let tag_false = BytesStart::from_content("elem xsi:nil=\"false\"", 4);
        assert!(!is_nil_element(&tag_false));

        let tag_regular = BytesStart::from_content("elem id=\"123\"", 4);
        assert!(!is_nil_element(&tag_regular));
    }

    #[test]
    fn test_xml_deserializer_from_rust() {
        pyo3::prepare_freethreaded_python();
        Python::with_gil(|py| {
            let code = r#"
from dataclasses import dataclass, field

@dataclass
class SimpleItem:
    id: int = field(metadata={"type": "Attribute"})
    name: str = field(default="")
"#;
            let _ = py.import_bound("typing").unwrap();
            let _ = py.import_bound("dataclasses").unwrap();
            let locals = pyo3::types::PyDict::new_bound(py);
            py.run_bound(code, Some(&locals), Some(&locals)).unwrap();
            let simple_item_cls = locals
                .get_item("SimpleItem")
                .unwrap()
                .unwrap()
                .downcast_into::<pyo3::types::PyType>()
                .unwrap();

            let schema = ModelSchema::from_py_class(&simple_item_cls).unwrap();
            let xml = b"<SimpleItem id=\"99\"><name>RustNative</name></SimpleItem>";
            let res = XmlDeserializer::deserialize(py, xml, schema).unwrap();
            let obj = res.bind(py);

            assert_eq!(obj.getattr("id").unwrap().extract::<i64>().unwrap(), 99);
            assert_eq!(
                obj.getattr("name").unwrap().extract::<String>().unwrap(),
                "RustNative"
            );
        });
    }

    #[test]
    fn test_xml_deserializer_malformed_xml() {
        pyo3::prepare_freethreaded_python();
        Python::with_gil(|py| {
            let code = r#"
from dataclasses import dataclass

@dataclass
class Dummy:
    pass
"#;
            let _ = py.import_bound("typing").unwrap();
            let _ = py.import_bound("dataclasses").unwrap();
            let locals = pyo3::types::PyDict::new_bound(py);
            py.run_bound(code, Some(&locals), Some(&locals)).unwrap();
            let dummy_cls = locals
                .get_item("Dummy")
                .unwrap()
                .unwrap()
                .downcast_into::<pyo3::types::PyType>()
                .unwrap();
            let schema = ModelSchema::from_py_class(&dummy_cls).unwrap();

            let malformed = b"<Dummy><unclosed>";
            assert!(XmlDeserializer::deserialize(py, malformed, schema).is_err());
        });
    }
}
