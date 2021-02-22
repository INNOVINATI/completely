def _element(e: object):
    if e or e == 0:
        return 1
    return 0


def _list(l: list):
    assert l
    return round(sum((measure(e) for e in l)) / len(l), 3)


def _set(s: set):
    assert s
    return _list(list(s))


def _dict(d: dict):
    assert d
    return _list(d.values())


def measure(o: object):
    if isinstance(o, (int, float, str)):
        return _element(o)
    if not o:
        return 0
    if isinstance(o, list):
        return _list(o)
    if isinstance(o, set):
        return _set(o)
    if isinstance(o, dict):
        return _dict(o)

    raise ValueError('Cannot analyze')
