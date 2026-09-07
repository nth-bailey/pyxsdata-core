# Contributing to pyxsdata-core

Thank you for your interest in contributing to `pyxsdata-core`! This repository houses the ultra-high-performance Rust core engine powering XML deserialization in `pyxsdata`.

---

## Code of Conduct

By participating in this project, you agree to abide by the terms of our [Code of Conduct](CODE_OF_CONDUCT.md). Please report any unacceptable behavior to [bailey.tan.nguyen@gmail.com](mailto:bailey.tan.nguyen@gmail.com).

---

## Getting Started

### Prerequisites

- **Rust**: Stable toolchain (install via [rustup](https://rustup.rs/)).
- **Python**: Python >= 3.12.
- **Maturin**: Build tool for PyO3 Rust extensions (`pip install maturin` or `uv pip install maturin`).

### Setting Up the Development Environment

1. Fork and clone the repository:
   ```bash
   git clone https://github.com/nth-bailey/pyxsdata-core.git
   cd pyxsdata-core
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   pip install maturin pytest pytest-benchmark pydantic ruff
   ```

3. Build and install the extension in development (editable) mode:
   ```bash
   maturin develop
   ```

   For optimized benchmark builds:
   ```bash
   maturin develop --release
   ```

---

## Development Workflow & Standards

### 1. Code Formatting & Linting

- **Rust Formatting**:
  ```bash
  cargo fmt --check
  ```
  Auto-format with:
  ```bash
  cargo fmt
  ```

- **Rust Clippy**:
  ```bash
  cargo clippy --all-targets -- -D warnings
  ```

- **Python Linting**:
  ```bash
  ruff check python/ tests/
  ```

### 2. Testing

- **Rust Unit Tests**:
  ```bash
  cargo test
  ```

- **Python Integration Tests**:
  ```bash
  pytest
  ```

### 3. Benchmarks

To run the deserialization benchmarks:
```bash
maturin develop --release
pytest --benchmark-only
```

---

## Commit Guidelines

We use [Conventional Commits](https://www.conventionalcommits.org/):

- `feat:` A new feature or parsing capability.
- `fix:` A bug fix.
- `perf:` Performance optimizations.
- `refactor:` Code restructuring without behavior changes.
- `docs:` Documentation improvements.
- `test:` Adding or updating tests.
- `chore:` Build, CI, or dependency updates.

Example:
```bash
git commit -m "perf(deserializer): optimize attribute string extraction using memchr"
```

---

## Submitting a Pull Request

1. Create a descriptive feature branch:
   ```bash
   git checkout -b perf/optimize-field-dispatch
   ```
2. Implement your changes along with corresponding tests.
3. Verify that `cargo fmt`, `cargo clippy`, `cargo test`, and `pytest` all pass.
4. Push your branch and submit a Pull Request to `main`.
