use crate::schema::ScalarType;
use pyo3::prelude::*;
use pyo3::types::PyString;

pub struct ValueConverter;

impl ValueConverter {
    pub fn parse_scalar<'py>(
        py: Python<'py>,
        scalar_type: &ScalarType,
        bytes: &[u8],
    ) -> PyResult<Bound<'py, PyAny>> {
        match scalar_type {
            ScalarType::String => {
                let s = std::str::from_utf8(bytes).map_err(|e| {
                    pyo3::exceptions::PyValueError::new_err(format!("Invalid UTF-8: {}", e))
                })?;
                Ok(PyString::new_bound(py, s).into_any())
            }
            ScalarType::Int => {
                let trimmed = trim_bytes(bytes);
                let val: i64 = lexical_core::parse(trimmed).map_err(|e| {
                    pyo3::exceptions::PyValueError::new_err(format!("Invalid integer: {:?}", e))
                })?;
                Ok(val.to_object(py).into_bound(py))
            }
            ScalarType::Float => {
                let trimmed = trim_bytes(bytes);
                let val: f64 = lexical_core::parse(trimmed).map_err(|e| {
                    pyo3::exceptions::PyValueError::new_err(format!("Invalid float: {:?}", e))
                })?;
                Ok(val.to_object(py).into_bound(py))
            }
            ScalarType::Bool => {
                let trimmed = trim_bytes(bytes);
                let b = match trimmed {
                    b"true" | b"1" => true,
                    b"false" | b"0" => false,
                    _ => {
                        return Err(pyo3::exceptions::PyValueError::new_err(format!(
                            "Invalid boolean literal: {:?}",
                            std::str::from_utf8(trimmed).unwrap_or("<invalid utf8>")
                        )))
                    }
                };
                Ok(b.to_object(py).into_bound(py))
            }
            ScalarType::XmlDate => {
                let s = std::str::from_utf8(trim_bytes(bytes)).map_err(|e| {
                    pyo3::exceptions::PyValueError::new_err(format!("Invalid UTF-8: {}", e))
                })?;
                // Parse YYYY-MM-DD
                if s.len() == 10 && s.as_bytes()[4] == b'-' && s.as_bytes()[7] == b'-' {
                    if let (Ok(y), Ok(m), Ok(d)) = (
                        s[0..4].parse::<i32>(),
                        s[5..7].parse::<u32>(),
                        s[8..10].parse::<u32>(),
                    ) {
                        let xml_date_cls = py
                            .import_bound("pyxsdata.models.datatype")?
                            .getattr("XmlDate")?;
                        return xml_date_cls.call1((y, m, d));
                    }
                }
                // Fallback to XmlDate.from_string
                let xml_date_cls = py
                    .import_bound("pyxsdata.models.datatype")?
                    .getattr("XmlDate")?;
                xml_date_cls.call_method1("from_string", (s,))
            }
            ScalarType::XmlDateTime => {
                let s = std::str::from_utf8(trim_bytes(bytes)).map_err(|e| {
                    pyo3::exceptions::PyValueError::new_err(format!("Invalid UTF-8: {}", e))
                })?;
                let xml_dt_cls = py
                    .import_bound("pyxsdata.models.datatype")?
                    .getattr("XmlDateTime")?;
                xml_dt_cls.call_method1("from_string", (s,))
            }
            ScalarType::Decimal => {
                let s = std::str::from_utf8(trim_bytes(bytes)).map_err(|e| {
                    pyo3::exceptions::PyValueError::new_err(format!("Invalid UTF-8: {}", e))
                })?;
                let decimal_cls = py.import_bound("decimal")?.getattr("Decimal")?;
                decimal_cls.call1((s,))
            }
            ScalarType::XmlTime => {
                let s = std::str::from_utf8(trim_bytes(bytes)).map_err(|e| {
                    pyo3::exceptions::PyValueError::new_err(format!("Invalid UTF-8: {}", e))
                })?;
                let xml_time_cls = py
                    .import_bound("pyxsdata.models.datatype")?
                    .getattr("XmlTime")?;
                xml_time_cls.call_method1("from_string", (s,))
            }
            ScalarType::XmlDuration => {
                let s = std::str::from_utf8(trim_bytes(bytes)).map_err(|e| {
                    pyo3::exceptions::PyValueError::new_err(format!("Invalid UTF-8: {}", e))
                })?;
                let xml_dur_cls = py
                    .import_bound("pyxsdata.models.datatype")?
                    .getattr("XmlDuration")?;
                xml_dur_cls.call1((s,))
            }

            ScalarType::Enum(ref enum_obj) => {
                let s = std::str::from_utf8(trim_bytes(bytes)).map_err(|e| {
                    pyo3::exceptions::PyValueError::new_err(format!("Invalid UTF-8: {}", e))
                })?;
                let cls = enum_obj.bind(py);
                if let Ok(val) = cls.call1((s,)) {
                    return Ok(val);
                }
                if let Ok(i) = s.parse::<i64>() {
                    if let Ok(val) = cls.call1((i,)) {
                        return Ok(val);
                    }
                }
                if let Ok(val) = cls.get_item(s) {
                    return Ok(val);
                }
                Err(pyo3::exceptions::PyValueError::new_err(format!(
                    "Cannot convert {:?} to enum {:?}",
                    s, cls
                )))
            }
            ScalarType::Any => {
                let s = std::str::from_utf8(bytes).map_err(|e| {
                    pyo3::exceptions::PyValueError::new_err(format!("Invalid UTF-8: {}", e))
                })?;
                Ok(PyString::new_bound(py, s).into_any())
            }
        }
    }
}

#[inline(always)]
fn trim_bytes(bytes: &[u8]) -> &[u8] {
    let mut start = 0;
    while start < bytes.len()
        && (bytes[start] == b' '
            || bytes[start] == b'\t'
            || bytes[start] == b'\n'
            || bytes[start] == b'\r')
    {
        start += 1;
    }
    let mut end = bytes.len();
    while end > start
        && (bytes[end - 1] == b' '
            || bytes[end - 1] == b'\t'
            || bytes[end - 1] == b'\n'
            || bytes[end - 1] == b'\r')
    {
        end -= 1;
    }
    &bytes[start..end]
}
