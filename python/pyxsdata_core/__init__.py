"""pyxsdata-core: High-performance native Rust core for pyxsdata."""

from pyxsdata_core._pyxsdata_core import (  # type: ignore[import-not-found]
    deserialize as _deserialize,
)
from pyxsdata_core._pyxsdata_core import (
    version as _version,
)

__version__ = _version()


def deserialize[T](source: bytes | str, target_type: type[T]) -> T:
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


__all__ = ["__version__", "deserialize"]
