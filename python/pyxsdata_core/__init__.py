"""pyxsdata-core: High-performance native Rust core for pyxsdata."""

from typing import Any, TypeVar

from pyxsdata_core._pyxsdata_core import (  # type: ignore[import-not-found]
    deserialize as _deserialize,
    version as _version,
)

__version__ = _version()
T = TypeVar("T")


def deserialize(source: bytes | str, target_type: type[T]) -> T:
    """Deserialize XML bytes or string into a Python dataclass or model instance.

    Args:
        source: XML content as raw bytes or a string.
        target_type: The target dataclass or model class.

    Returns:
        The deserialized model instance.
    """
    if isinstance(source, str):
        source = source.encode("utf-8")
    return _deserialize(source, target_type)


__all__ = ["deserialize", "__version__"]
