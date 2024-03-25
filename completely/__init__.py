from typing import Any, Union


def _atomic(v: Union[str, int, float]) -> float:
    """Check if an atomic value is set.

    Args:
        v (Union[str, int, float]): An atomic value.

    Returns:
        float: 1.0 if the value is set, 0.0 otherwise.
    """
    return 1 if v is not None and v or v == 0 else 0


def _list(ls: list) -> float:
    """Check completeness of a list

    Args:
        ls (list): Input list

    Returns:
        float: Completeness percentage
    """
    assert ls
    return round(sum((measure(e) for e in ls)) / len(ls), 3)


def _set(s: set):
    """Check completeness of a set

    Args:
        s (set): Input set

    Returns:
        float: Completeness percentage
    """
    assert s
    return _list(list(s))


def _dict(d: dict):
    """Check completeness of a dictionary

    Args:
        d (dict): Input dictionary

    Returns:
        float: Completeness percentage
    """
    assert d
    return _list(d.values())


def measure(data: Any) -> float:
    """Main routine to measure data completeness

    Args:
        data (Any): Input data

    Raises:
        ValueError: Unsupported data type

    Returns:
        float: Completeness percentage
    """
    if isinstance(data, (int, float, str)):
        return _atomic(data)
    if not data:
        return 0
    if isinstance(data, list):
        return _list(data)
    if isinstance(data, set):
        return _set(data)
    if isinstance(data, dict):
        return _dict(data)

    raise ValueError(f"Cannot handle input of type {type(data)}")
