#![allow(clippy::useless_conversion, clippy::manual_pop_if)]

use pyo3::prelude::*;
use pyo3::types::PyType;
use std::collections::HashMap;
use std::sync::{Arc, RwLock};

mod converters;
mod parser;
mod schema;

use parser::XmlDeserializer;
use schema::ModelSchema;

// Global thread-safe schema cache keyed by Python type pointer
static SCHEMA_CACHE: RwLock<Option<HashMap<usize, Arc<ModelSchema>>>> = RwLock::new(None);

fn get_or_create_schema<'py>(cls: &Bound<'py, PyType>) -> PyResult<Arc<ModelSchema>> {
    let type_key = cls.as_ptr() as usize;

    // Check read lock
    {
        let cache = SCHEMA_CACHE.read().unwrap();
        if let Some(ref map) = *cache {
            if let Some(schema) = map.get(&type_key) {
                return Ok(Arc::clone(schema));
            }
        }
    }

    // Build schema
    let schema = ModelSchema::from_py_class(cls)?;

    // Write lock
    {
        let mut cache = SCHEMA_CACHE.write().unwrap();
        let map = cache.get_or_insert_with(HashMap::new);
        map.insert(type_key, Arc::clone(&schema));
    }

    Ok(schema)
}

#[pyfunction]
fn deserialize<'py>(
    py: Python<'py>,
    source: &[u8],
    target_type: Bound<'py, PyType>,
) -> PyResult<PyObject> {
    let schema = get_or_create_schema(&target_type)?;
    XmlDeserializer::deserialize(py, source, schema)
}

#[pyfunction]
fn version() -> &'static str {
    env!("CARGO_PKG_VERSION")
}

#[pymodule]
fn _pyxsdata_core(m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(deserialize, m)?)?;
    m.add_function(wrap_pyfunction!(version, m)?)?;
    Ok(())
}
