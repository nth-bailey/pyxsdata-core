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

#[cfg(test)]
mod tests {
    use super::*;
    use std::sync::Arc;

    #[test]
    fn test_trim_bytes_variations() {
        assert_eq!(trim_bytes(b""), b"");
        assert_eq!(trim_bytes(b"   \r\n\t  "), b"");
        assert_eq!(trim_bytes(b"hello"), b"hello");
        assert_eq!(trim_bytes(b"  hello  "), b"hello");
        assert_eq!(trim_bytes(b"\n\t\r  world  \r\n"), b"world");
        assert_eq!(trim_bytes(b"a b c"), b"a b c");
    }

    #[test]
    fn test_parse_scalar_primitives() {
        pyo3::prepare_freethreaded_python();
        Python::with_gil(|py| {
            // String
            let res = ValueConverter::parse_scalar(py, &ScalarType::String, b"  abc  ").unwrap();
            assert_eq!(res.extract::<String>().unwrap(), "  abc  ");

            let invalid_utf8 = [0xFF, 0xFE];
            assert!(ValueConverter::parse_scalar(py, &ScalarType::String, &invalid_utf8).is_err());

            // Int
            let res = ValueConverter::parse_scalar(py, &ScalarType::Int, b" 42 \n").unwrap();
            assert_eq!(res.extract::<i64>().unwrap(), 42);

            let res_neg = ValueConverter::parse_scalar(py, &ScalarType::Int, b"-100").unwrap();
            assert_eq!(res_neg.extract::<i64>().unwrap(), -100);

            assert!(ValueConverter::parse_scalar(py, &ScalarType::Int, b"not_an_int").is_err());

            // Float
            let res = ValueConverter::parse_scalar(py, &ScalarType::Float, b" 3.1415 ").unwrap();
            assert!((res.extract::<f64>().unwrap() - 3.1415).abs() < 1e-6);

            let res_sci = ValueConverter::parse_scalar(py, &ScalarType::Float, b"1e-3").unwrap();
            assert!((res_sci.extract::<f64>().unwrap() - 0.001).abs() < 1e-6);

            assert!(
                ValueConverter::parse_scalar(py, &ScalarType::Float, b"invalid_float").is_err()
            );

            // Bool
            for (lit, expected) in [
                (&b"true"[..], true),
                (&b"1"[..], true),
                (&b"  true  "[..], true),
                (&b"false"[..], false),
                (&b"0"[..], false),
                (&b"  0\n"[..], false),
            ] {
                let res = ValueConverter::parse_scalar(py, &ScalarType::Bool, lit).unwrap();
                assert_eq!(res.extract::<bool>().unwrap(), expected);
            }
            assert!(ValueConverter::parse_scalar(py, &ScalarType::Bool, b"yes").is_err());

            // Any
            let res = ValueConverter::parse_scalar(py, &ScalarType::Any, b"hello").unwrap();
            assert_eq!(res.extract::<String>().unwrap(), "hello");
        });
    }

    #[test]
    fn test_parse_scalar_complex_types() {
        pyo3::prepare_freethreaded_python();
        Python::with_gil(|py| {
            // Decimal
            let res = ValueConverter::parse_scalar(py, &ScalarType::Decimal, b" 123.456 ").unwrap();
            let str_val = res.str().unwrap().to_string();
            assert_eq!(str_val, "123.456");

            // Enum
            let code = "from enum import Enum\nclass Color(Enum):\n    RED = 'RED'\n    BLUE = 2\n";
            let locals = pyo3::types::PyDict::new_bound(py);
            py.run_bound(code, None, Some(&locals)).unwrap();
            let color_cls = locals
                .get_item("Color")
                .unwrap()
                .unwrap()
                .into_any()
                .unbind();
            let enum_type = ScalarType::Enum(Arc::new(color_cls));

            // string member lookup
            let res = ValueConverter::parse_scalar(py, &enum_type, b"RED").unwrap();
            assert_eq!(
                res.getattr("value").unwrap().extract::<String>().unwrap(),
                "RED"
            );

            // int member lookup
            let res = ValueConverter::parse_scalar(py, &enum_type, b"2").unwrap();
            assert_eq!(res.getattr("value").unwrap().extract::<i64>().unwrap(), 2);

            // invalid enum
            assert!(ValueConverter::parse_scalar(py, &enum_type, b"GREEN").is_err());
        });
    }

    #[test]
    fn test_parse_scalar_dates() {
        pyo3::prepare_freethreaded_python();
        Python::with_gil(|py| {
            if py.import_bound("pyxsdata.models.datatype").is_err() {
                // pyxsdata not installed in this environment
                return;
            }
            // XmlDate fast path
            let res =
                ValueConverter::parse_scalar(py, &ScalarType::XmlDate, b"2024-05-15").unwrap();
            let str_val = res.str().unwrap().to_string();
            assert_eq!(str_val, "2024-05-15");

            // XmlDate with timezone (fallback)
            let res_fallback =
                ValueConverter::parse_scalar(py, &ScalarType::XmlDate, b"2024-05-15Z").unwrap();
            let str_val = res_fallback.str().unwrap().to_string();
            assert_eq!(str_val, "2024-05-15Z");

            // XmlDateTime
            let res =
                ValueConverter::parse_scalar(py, &ScalarType::XmlDateTime, b"2024-05-15T12:30:00Z")
                    .unwrap();
            let str_val = res.str().unwrap().to_string();
            assert_eq!(str_val, "2024-05-15T12:30:00Z");

            // XmlTime
            let res = ValueConverter::parse_scalar(py, &ScalarType::XmlTime, b"12:30:00").unwrap();
            let str_val = res.str().unwrap().to_string();
            assert_eq!(str_val, "12:30:00");

            // XmlDuration
            let res =
                ValueConverter::parse_scalar(py, &ScalarType::XmlDuration, b"P1Y2M3D").unwrap();
            let str_val = res.str().unwrap().to_string();
            assert_eq!(str_val, "P1Y2M3D");
        });
    }
}
