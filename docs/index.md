# pyxsdata-core

<p align="center">
  <strong>Blazing-Fast Native Rust XML Deserializer for Python</strong><br>
  <em>Accelerating dataclasses and Pydantic v2 with PyO3 & quick-xml</em>
</p>

---

## What is `pyxsdata-core`?

**`pyxsdata-core`** is a dedicated native acceleration library written in Rust using [PyO3](https://pyo3.rs) and [`quick-xml`](https://github.com/tafia/quick-xml). It delivers high-throughput XML deserialization for Python by bypassing the traditional DOM allocation, intermediate node wrapping, and generic Python event pumps used by standard XML parsers.

Instead, `pyxsdata-core` compiles Python class introspection into an in-memory Rust schema registry. As XML tokens stream through `quick-xml`'s zero-copy pull parser, Rust directly instantiates Python dataclass and Pydantic v2 objects via the CPython C-API at rates exceeding **300,000 objects per second**.

```mermaid
flowchart LR
    A[XML Document / Bytes] --> B[quick-xml Tokenizer]
    B --> C[Rust Schema Registry]
    C -->|Direct PyO3 C-API Call| D[Python dataclasses / Pydantic v2]
    
    style C fill:#f96,stroke:#333,stroke-width:2px
```

---

## Key Highlights

- **Extreme Performance**:
  - **~311,000 objects/sec** for Pydantic v2 models (**7.7x faster** than pure Python).
  - **~290,000 objects/sec** for standard dataclasses (**9.5x faster** than pure Python, **15x faster** than legacy `xsdata`).
- **Native Pydantic v2 & Dataclass Support**: Works seamlessly with both standard library `@dataclass` models and `pydantic.BaseModel` schemas without configuration shims.
- **Zero Intermediate DOM Allocation**: No `xml.etree.Element`, `lxml.etree.Element`, or intermediate event queues created during the parse pass.
- **Precompiled Multi-Platform Wheels**: Ready-to-use binaries on Linux (x86_64, aarch64), macOS (Apple Silicon, Intel), and Windows (x64) for Python 3.12+.
- **Drop-in Acceleration for `pyxsdata`**: Powers `CoreXmlParser` and `CoreEventHandler` in `pyxsdata[core]`.

---

## At a Glance

=== "Pydantic v2"

    ```python
    from pydantic import BaseModel
    import pyxsdata_core

    class Item(BaseModel):
        id: int
        name: str
        price: float

    xml = b"<Item><id>42</id><name>Widget</name><price>19.99</price></Item>"
    item = pyxsdata_core.deserialize(xml, Item)

    print(item)
    # Item(id=42, name='Widget', price=19.99)
    ```

=== "Standard Dataclasses"

    ```python
    from dataclasses import dataclass
    import pyxsdata_core

    @dataclass
    class Item:
        id: int
        name: str
        price: float

    xml = b"<Item><id>42</id><name>Widget</name><price>19.99</price></Item>"
    item = pyxsdata_core.deserialize(xml, Item)

    print(item)
    # Item(id=42, name='Widget', price=19.99)
    ```

=== "With pyxsdata"

    ```python
    from pyxsdata.pydantic import CoreXmlParser
    # or: from pyxsdata.formats.dataclass.parsers import CoreXmlParser

    parser = CoreXmlParser()
    item = parser.from_bytes(xml, Item)
    ```

---

## Documentation Guide

- [**5-Minute Quickstart**](quickstart.md): Learn how to deserialize XML into Python models in seconds.
- [**Installation**](installation.md): Wheel availability, pip/uv installation, and building from source.
- [**Performance & Benchmarks**](benchmarks.md): Detailed throughput numbers, flamegraphs, and comparative graphs.
- [**Architecture & Design**](architecture.md): Deep dive into the Rust schema engine and PyO3 C-API integration.
- [**Integration with pyxsdata**](integration.md): How `pyxsdata` uses `pyxsdata-core` as a high-speed engine.
- [**Python API Reference**](api.md): Complete signature documentation for all exported functions and classes.
