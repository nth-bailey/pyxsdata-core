# AGENTS.md

Instructions and guidelines for AI coding assistants working in the `pyxsdata-core`
repository.

---

## 1. Project Overview

`pyxsdata-core` is the high-performance native Rust engine for `pyxsdata`, providing
ultra-fast XML deserialization directly into Python `dataclasses` and Pydantic v2
models.

- **Technology**: Rust 2021, PyO3 (`abi3-py312`), `quick-xml`, `lexical-core`,
  `smallvec`.
- **Repository**: `nth-bailey/pyxsdata-core`
- **Supported Python**: `Python >= 3.12` exclusively.
- **Maintainer**: Bailey Nguyen (`bailey.tan.nguyen@gmail.com`).

---

## 2. Core Architectural Decisions & Invariants

When contributing or refactoring, strictly maintain the following invariants:

1. **Python ABI3 Portability (`abi3-py312`)**:
   - The native extension is compiled against the stable Python 3.12+ ABI (`abi3`).
   - Do not introduce non-limited C-API calls that violate `abi3-py312` compatibility.

2. **Zero Unnecessary Allocations**:
   - Stream XML tokens using `quick-xml` reader events.
   - Use `lexical-core` for high-throughput integer and float conversions from byte
     slices.
   - Avoid allocating intermediate Python dictionaries whenever instantiating target
     classes; construct model instances directly via PyO3 constructor invocations.

3. **Dual Model Support (Dataclasses & Pydantic v2)**:
   - Schema introspection must support standard Python `dataclasses` (via
     `__dataclass_fields__`) and Pydantic v2 models (via `model_fields`).
   - Field metadata respects both `xsdata_metadata` and `json_schema_extra`.

4. **100% Code Coverage**:
   - All Python wrapper code in `python/pyxsdata_core/` must maintain **100%
     statement and branch test coverage** (`fail_under = 100` in `pyproject.toml`).
   - Every feature or bug fix must include corresponding tests in `tests/`.

---

## 3. Tooling & Development Workflow

### Rust Toolchain & Build

- Stable Rust toolchain managed via `rustup`.
- Build in editable development mode:
  ```bash
  maturin develop
  ```
- Build optimized release for benchmarking:
  ```bash
  maturin develop --release
  ```

### Linting & Formatting

- **Rust Formatting**:
  ```bash
  cargo fmt --check
  ```
  Auto-format with `cargo fmt`.
- **Rust Clippy**:
  ```bash
  cargo clippy --all-targets -- -D warnings
  ```
- **Python Linting**:
  ```bash
  ruff check python/ tests/
  ```

### Testing & Coverage

- **Rust Unit & Integration Tests**:
  ```bash
  cargo test
  ```
- **Python Integration Tests & Coverage (100% Enforced)**:
  ```bash
  pytest --cov
  ```
- **Performance Benchmarks**:
  ```bash
  pytest --benchmark-only
  ```

### Documentation: Zensical

- Documentation is powered by **Zensical** static site generator.
- Configuration: `zensical.toml`.
- Build:
  ```bash
  zensical build
  ```

---

## 4. Repository Structure

```
pyxsdata-core/
├── Cargo.toml                     # Rust package manifest and profile configs
├── pyproject.toml                 # Maturin and pytest/coverage configurations
├── src/
│   ├── lib.rs                     # PyO3 module initialization (_pyxsdata_core)
│   ├── schema.rs                  # Python dataclass/Pydantic model schema extractor
│   ├── parser.rs                  # quick-xml streaming deserializer engine
│   └── converters.rs              # Byte-slice to scalar type converters
├── python/
│   └── pyxsdata_core/
│       ├── __init__.py            # High-level Python API (deserialize, __version__)
│       └── py.typed               # PEP 561 typing marker
├── tests/
│   └── test_core.py               # Python end-to-end integration & unit tests
├── docs/                          # Zensical documentation markdown files
├── .github/                       # GitHub workflows, funding, issue/PR templates
└── zensical.toml                  # Documentation configuration
```

---

## 5. Agent Etiquette & Verification Checklist

Before completing any task:

1. **Rust Format**: Ensure `cargo fmt --check` passes with zero differences.
2. **Rust Clippy**: Ensure `cargo clippy --all-targets -- -D warnings` produces 0
   warnings.
3. **Rust Tests**: Ensure `cargo test` passes cleanly.
4. **Python Tests & Coverage**: Ensure `pytest --cov` passes with **100% coverage**.
5. **Python Lint**: Ensure `ruff check python/ tests/` passes with 0 errors.
6. **Docs**: If documentation is modified, ensure `zensical build` succeeds.
