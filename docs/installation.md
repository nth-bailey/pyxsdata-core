# Installation

`pyxsdata-core` is distributed as multi-platform precompiled binary wheels for CPython 3.12+ and as a source distribution (`sdist`).

---

## Package Manager Installation

Install the latest stable release from PyPI:

=== "uv"

    ```console
    $ uv add pyxsdata-core
    ```

=== "pip"

    ```console
    $ pip install pyxsdata-core
    ```

=== "poetry"

    ```console
    $ poetry add pyxsdata-core
    ```

---

## Binary Wheel Availability

Every release of `pyxsdata-core` builds and tests binary wheels using GitHub Actions and `maturin-action`:

| Operating System | Architecture | Binary Tag | Notes |
| :--- | :--- | :--- | :--- |
| **Linux** | `x86_64` (AMD64) | `manylinux_2_17_x86_64` | Compatible with all modern Linux distros (Ubuntu, Debian, RHEL, Alpine glibc) |
| **Linux** | `aarch64` (ARM64) | `manylinux_2_17_aarch64` | AWS Graviton, Raspberry Pi 4+, Linux on Apple Silicon |
| **macOS** | `arm64` (Apple Silicon) | `macosx_11_0_arm64` | Native M1, M2, M3, M4 Macs |
| **macOS** | `x86_64` (Intel) | `macosx_10_12_x86_64` | Legacy Intel Macs |
| **Windows** | `x86_64` (AMD64) | `win_amd64` | Windows 10, 11, Windows Server |

---

## Installing with `pyxsdata`

If you are using `pyxsdata`, install the `core` extra to automatically install `pyxsdata-core` and wire up the `CoreXmlParser` and `CoreEventHandler` backends:

```console
$ uv add "pyxsdata[core]"
# or
$ pip install "pyxsdata[core]"
```

---

## Building from Source

If you are developing `pyxsdata-core` or targeting an unsupported architecture, you can compile from source using Rust and Maturin.

### Prerequisites

- **Python**: `>= 3.12`
- **Rust Toolchain**: `>= 1.80` ([Install via rustup](https://rustup.rs))
- **Maturin**: `>= 1.5.0`

### Build Steps

```console
# Clone repository
$ git clone https://github.com/nth-bailey/pyxsdata-core.git
$ cd pyxsdata-core

# Create virtual environment
$ python3 -m venv .venv
$ source .venv/bin/activate

# Install build tooling and dev dependencies
$ pip install maturin pytest pyxsdata pydantic

# Build and install extension in release mode
$ maturin develop --release

# Run test suite
$ pytest
```
