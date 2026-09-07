# Python API Reference

Complete reference for all functions and classes exposed by the `pyxsdata_core` module.

---

## `deserialize()`

::: pyxsdata_core.deserialize

```python
def deserialize(source: str | bytes, model_class: type[T]) -> T: ...
```

Deserializes an XML document into an instance of `model_class`.

### Parameters

- **`source`** (`str | bytes`): The XML document content as a UTF-8 string or raw bytes.
- **`model_class`** (`type[T]`): The target model class to instantiate. Supported types:
  - Standard library `@dataclass` classes.
  - Pydantic v2 `BaseModel` subclasses.

### Returns

- **`T`**: A newly instantiated instance of `model_class` populated with the data from the XML document.

### Raises

- **`ValueError`**: If the XML syntax is malformed, root element tags do not match the expected schema, or required fields cannot be parsed.
- **`TypeError`**: If `model_class` is not a valid dataclass or Pydantic model.

### Example

```python
from dataclasses import dataclass
import pyxsdata_core

@dataclass
class Book:
    title: str
    pages: int

xml = b"<Book><title>The Odyssey</title><pages>450</pages></Book>"
book = pyxsdata_core.deserialize(xml, Book)
assert book.title == "The Odyssey"
assert book.pages == 450
```

---

## `ModelSchema`

```python
class ModelSchema:
    def __init__(self, model_class: type) -> None: ...
    def deserialize(self, source: str | bytes) -> Any: ...
```

An in-memory compiled Rust representation of a Python model's XML schema. Precompiling a `ModelSchema` avoids class introspection and reflection overhead during high-volume parsing loops.

### Methods

#### `__init__(model_class: type)`
Compiles the target dataclass or Pydantic model structure into Rust field mappings.

#### `deserialize(source: str | bytes) -> Any`
Parses the input XML bytes or string using the precompiled schema and returns a new Python instance.

### Example

```python
import pyxsdata_core
from myapp.models import MetricEvent

# Precompile once at application startup
metric_schema = pyxsdata_core.ModelSchema(MetricEvent)

# Process high-frequency incoming XML events
def handle_event(raw_bytes: bytes):
    event = metric_schema.deserialize(raw_bytes)
    store(event)
```
