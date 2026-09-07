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
    XmlDate,
    XmlDateTime,
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
        let fields_dict = cls.getattr("__dataclass_fields__")?;
        let dict: Bound<'py, PyDict> = fields_dict.downcast_into()?;

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

            // Extract type annotation
            let field_type_obj = field_obj.getattr("type")?;
            let val_type = Self::resolve_value_type(py, &field_type_obj)?;

            let idx = fields.len();
            let xml_name = xml_name_str.into_bytes();

            match kind {
                FieldKind::Attribute => {
                    attribute_map.insert(xml_name.clone(), idx);
                }
                FieldKind::Element => {
                    element_map.insert(xml_name.clone(), idx);
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
            "XmlDate" => Ok(ValueType::Scalar(ScalarType::XmlDate)),
            "XmlDateTime" => Ok(ValueType::Scalar(ScalarType::XmlDateTime)),
            _ => {
                // Check if it is another dataclass
                if type_obj.hasattr("__dataclass_fields__")? {
                    if let Ok(cls) = type_obj.downcast::<PyType>() {
                        let nested = Self::from_py_class(cls)?;
                        return Ok(ValueType::Nested(nested));
                    }
                }
                Ok(ValueType::Scalar(ScalarType::Any))
            }
        }
    }
}
