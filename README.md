# pyxsdata-core

High-performance native Rust core for [`pyxsdata`](https://github.com/nth-bailey/pyxsdata).

## Overview

`pyxsdata-core` provides streaming, zero-allocation native XML deserialization into Python dataclasses and Pydantic models. Built with [PyO3](https://pyo3.rs) and [`quick-xml`](https://github.com/tafia/quick-xml), it delivers 150,000+ objects/sec throughput by processing XML tokens, stack management, and scalar conversion in Rust before constructing Python dataclasses via C-API.

## Installation

```bash
pip install pyxsdata-core
```

Or install with `pyxsdata`:

```bash
pip install "pyxsdata[core]"
```

## Development

Requires Rust 1.80+ and Python 3.12+.

```bash
# Install maturin
uv pip install maturin

# Build and develop
maturin develop
```

## License

MIT
