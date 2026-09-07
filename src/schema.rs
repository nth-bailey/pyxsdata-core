use pyo3::prelude::*;
use pyo3::types::{PyDict, PyString, PyType};
use std::collections::HashMap;
use std::sync::Arc;

#[derive(Debug, Clone, PartialEq, Eq)]
pub enum FieldKind {
    Attribute,
    Element,
    Text,
}

#[derive(Debug, Clone)]
pub enum ScalarType {
    String,
    Int,
    Float,
    Bool,
    Decimal,
    XmlDate,
    XmlDateTime,
    XmlTime,
    XmlDuration,
    Enum(Arc<PyObject>),
    Any,
}

#[derive(Debug, Clone)]
pub enum ValueType {
    Scalar(ScalarType),
    List(Box<ValueType>),
    Nested(Arc<ModelSchema>),
}

#[derive(Debug)]
#[allow(dead_code)]
pub struct FieldSchema {
    pub py_name: String,
    pub py_name_obj: PyObject,
    pub xml_name: Vec<u8>,
    pub kind: FieldKind,
    pub val_type: ValueType,
    pub is_init: bool,
}

#[derive(Debug)]
pub struct ModelSchema {
    pub py_class: PyObject,
    pub fields: Vec<FieldSchema>,
    pub element_map: HashMap<Vec<u8>, usize>,
    pub attribute_map: HashMap<Vec<u8>, usize>,
    pub text_field: Option<usize>,
}

impl ModelSchema {
    pub fn from_py_class<'py>(cls: &Bound<'py, PyType>) -> PyResult<Arc<Self>> {
        let py = cls.py();

        if cls.hasattr("model_fields")? {
            let model_fields = cls.getattr("model_fields")?;
            let dict: Bound<'py, PyDict> = model_fields.downcast_into()?;

            let mut fields = Vec::new();
            let mut element_map = HashMap::new();
            let mut attribute_map = HashMap::new();
            let mut text_field = None;

            for (field_name_obj, field_obj) in dict.iter() {
                let py_name: String = field_name_obj.extract()?;
                let py_name_py_str = PyString::new_bound(py, &py_name).into_any().unbind();

                let mut xml_name_str = py_name.clone();
                let mut kind = FieldKind::Element;

                // Check xsdata_metadata or json_schema_extra or metadata
                let metadata = field_obj
                    .getattr("xsdata_metadata")
                    .ok()
                    .or_else(|| field_obj.getattr("json_schema_extra").ok());

                if let Some(ref meta) = metadata {
                    if let Ok(type_val) = meta.get_item("type") {
                        let type_str: String = type_val.extract().unwrap_or_default();
                        match type_str.as_str() {
                            "Attribute" => kind = FieldKind::Attribute,
                            "Text" => kind = FieldKind::Text,
                            _ => kind = FieldKind::Element,
                        }
                    }
                    if let Ok(name_val) = meta.get_item("name") {
                        xml_name_str = name_val.extract().unwrap_or(py_name.clone());
                    }
                }

                let field_type_obj = field_obj.getattr("annotation")?;
                let val_type = Self::resolve_value_type(py, &field_type_obj)?;

                let idx = fields.len();
                let xml_name = xml_name_str.into_bytes();

                match kind {
                    FieldKind::Attribute => {
                        attribute_map.insert(xml_name.clone(), idx);
                        if let Some(pos) = xml_name.iter().position(|&b| b == b':') {
                            attribute_map.insert(xml_name[pos + 1..].to_vec(), idx);
                        }
                    }
                    FieldKind::Element => {
                        element_map.insert(xml_name.clone(), idx);
                        if let Some(pos) = xml_name.iter().position(|&b| b == b':') {
                            element_map.insert(xml_name[pos + 1..].to_vec(), idx);
                        }
                    }
                    FieldKind::Text => {
                        text_field = Some(idx);
                    }
                }

                fields.push(FieldSchema {
                    py_name,
                    py_name_obj: py_name_py_str,
                    xml_name,
                    kind,
                    val_type,
                    is_init: true,
                });
            }

            return Ok(Arc::new(ModelSchema {
                py_class: cls.clone().into_any().unbind(),
                fields,
                element_map,
                attribute_map,
                text_field,
            }));
        }

        let fields_dict = cls.getattr("__dataclass_fields__")?;
        let dict: Bound<'py, PyDict> = fields_dict.downcast_into()?;

        let type_hints: Option<Bound<'py, PyDict>> = py
            .import_bound("typing")
            .ok()
            .and_then(|m| m.getattr("get_type_hints").ok())
            .and_then(|f| f.call1((cls,)).ok())
            .and_then(|h| h.downcast_into::<PyDict>().ok());

        let mut fields = Vec::new();
        let mut element_map = HashMap::new();
        let mut attribute_map = HashMap::new();
        let mut text_field = None;

        for (field_name_obj, field_obj) in dict.iter() {
            let py_name: String = field_name_obj.extract()?;
            let py_name_py_str = PyString::new_bound(py, &py_name).into_any().unbind();

            // Extract metadata if any
            let metadata = field_obj.getattr("metadata").ok();
            let mut xml_name_str = py_name.clone();
            let mut kind = FieldKind::Element;

            if let Some(meta) = metadata {
                if let Ok(type_val) = meta.get_item("type") {
                    let type_str: String = type_val.extract().unwrap_or_default();
                    match type_str.as_str() {
                        "Attribute" => kind = FieldKind::Attribute,
                        "Text" => kind = FieldKind::Text,
                        _ => kind = FieldKind::Element,
                    }
                }
                if let Ok(name_val) = meta.get_item("name") {
                    xml_name_str = name_val.extract().unwrap_or(py_name.clone());
                }
            }

            let is_init: bool = field_obj
                .getattr("init")
                .and_then(|v| v.extract())
                .unwrap_or(true);

            // Extract type annotation (using type_hints for PEP 563 string annotations if available)
            let field_type_obj = if let Some(ref hints) = type_hints {
                if let Ok(Some(hint)) = hints.get_item(&field_name_obj) {
                    hint
                } else {
                    field_obj.getattr("type")?
                }
            } else {
                field_obj.getattr("type")?
            };
            let val_type = Self::resolve_value_type(py, &field_type_obj)?;

            let idx = fields.len();
            let xml_name = xml_name_str.into_bytes();

            match kind {
                FieldKind::Attribute => {
                    attribute_map.insert(xml_name.clone(), idx);
                    if let Some(pos) = xml_name.iter().position(|&b| b == b':') {
                        attribute_map.insert(xml_name[pos + 1..].to_vec(), idx);
                    }
                }
                FieldKind::Element => {
                    element_map.insert(xml_name.clone(), idx);
                    if let Some(pos) = xml_name.iter().position(|&b| b == b':') {
                        element_map.insert(xml_name[pos + 1..].to_vec(), idx);
                    }
                }
                FieldKind::Text => {
                    text_field = Some(idx);
                }
            }

            fields.push(FieldSchema {
                py_name,
                py_name_obj: py_name_py_str,
                xml_name,
                kind,
                val_type,
                is_init,
            });
        }

        Ok(Arc::new(ModelSchema {
            py_class: cls.clone().into_any().unbind(),
            fields,
            element_map,
            attribute_map,
            text_field,
        }))
    }

    fn resolve_value_type<'py>(
        py: Python<'py>,
        type_obj: &Bound<'py, PyAny>,
    ) -> PyResult<ValueType> {
        let type_name = if let Ok(name) = type_obj.getattr("__name__") {
            name.extract::<String>().unwrap_or_default()
        } else {
            type_obj.to_string()
        };

        // Check if parameterized type (list, Union/Optional, etc.)
        if let Ok(args) = type_obj.getattr("__args__") {
            if let Ok(tuple) = args.downcast_into::<pyo3::types::PyTuple>() {
                if type_name == "list" || type_name.starts_with("list[") {
                    if !tuple.is_empty() {
                        let inner = tuple.get_item(0)?;
                        let inner_val_type = Self::resolve_value_type(py, &inner)?;
                        return Ok(ValueType::List(Box::new(inner_val_type)));
                    }
                    return Ok(ValueType::List(Box::new(ValueType::Scalar(
                        ScalarType::Any,
                    ))));
                }

                // Union / Optional (e.g. T | None)
                let none_type = py.None().bind(py).get_type();
                let non_none: Vec<Bound<'py, PyAny>> =
                    tuple.iter().filter(|item| !item.is(&none_type)).collect();
                if non_none.len() == 1 {
                    return Self::resolve_value_type(py, &non_none[0]);
                }
            }
        }

        match type_name.as_str() {
            "str" => Ok(ValueType::Scalar(ScalarType::String)),
            "int" => Ok(ValueType::Scalar(ScalarType::Int)),
            "float" => Ok(ValueType::Scalar(ScalarType::Float)),
            "bool" => Ok(ValueType::Scalar(ScalarType::Bool)),
            "Decimal" => Ok(ValueType::Scalar(ScalarType::Decimal)),
            "XmlDate" => Ok(ValueType::Scalar(ScalarType::XmlDate)),
            "XmlDateTime" => Ok(ValueType::Scalar(ScalarType::XmlDateTime)),
            "XmlTime" => Ok(ValueType::Scalar(ScalarType::XmlTime)),
            "XmlDuration" => Ok(ValueType::Scalar(ScalarType::XmlDuration)),
            _ => {
                // Check if it is an Enum
                if let Ok(cls) = type_obj.downcast::<PyType>() {
                    if let Ok(enum_module) = py.import_bound("enum") {
                        if let Ok(enum_cls) = enum_module.getattr("Enum") {
                            if cls.is_subclass(&enum_cls).unwrap_or(false) {
                                return Ok(ValueType::Scalar(ScalarType::Enum(Arc::new(
                                    cls.clone().into_any().unbind(),
                                ))));
                            }
                        }
                    }
                    // Check if it is another dataclass or Pydantic model
                    if type_obj.hasattr("__dataclass_fields__")?
                        || type_obj.hasattr("model_fields")?
                    {
                        let nested = Self::from_py_class(cls)?;
                        return Ok(ValueType::Nested(nested));
                    }
                }
                Ok(ValueType::Scalar(ScalarType::Any))
            }
        }
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_model_schema_building_and_mapping() {
        pyo3::prepare_freethreaded_python();
        Python::with_gil(|py| {
            let _ = py.import_bound("typing").unwrap();
            let _ = py.import_bound("dataclasses").unwrap();

            let code = r#"
from dataclasses import dataclass, field

@dataclass
class ChildModel:
    age: int = 10

@dataclass
class ComplexModel:
    attr_id: str = field(metadata={"name": "ns:id", "type": "Attribute"})
    child: ChildModel | None = field(default=None, metadata={"name": "ns:child", "type": "Element"})
    tags: list[str] = field(default_factory=list, metadata={"name": "tag", "type": "Element"})
    description: str = field(default="", metadata={"type": "Text"})
"#;
            let locals = pyo3::types::PyDict::new_bound(py);
            py.run_bound(code, Some(&locals), Some(&locals)).unwrap();
            let complex_cls = locals
                .get_item("ComplexModel")
                .unwrap()
                .unwrap()
                .downcast_into::<pyo3::types::PyType>()
                .unwrap();

            let schema = ModelSchema::from_py_class(&complex_cls).unwrap();

            // Check attribute map (both prefixed and stripped)
            assert!(schema.attribute_map.contains_key(&b"ns:id"[..]));
            assert!(schema.attribute_map.contains_key(&b"id"[..]));

            // Check element map (both prefixed and stripped)
            assert!(schema.element_map.contains_key(&b"ns:child"[..]));
            assert!(schema.element_map.contains_key(&b"child"[..]));
            assert!(schema.element_map.contains_key(&b"tag"[..]));

            // Check text field index
            assert!(schema.text_field.is_some());
            let text_idx = schema.text_field.unwrap();
            assert_eq!(schema.fields[text_idx].py_name, "description");
        });
    }

    #[test]
    fn test_model_schema_rejects_non_model() {
        pyo3::prepare_freethreaded_python();
        Python::with_gil(|py| {
            let int_type = py.get_type_bound::<pyo3::types::PyInt>();
            assert!(ModelSchema::from_py_class(&int_type).is_err());
        });
    }
}
