from typing import List


def _dicts(ls: List[dict]):
    size = len(ls)
    total_score = 0
    for element in ls:
        sub_size = len(element)
        abs_score = sum([1 if bool(value) else 0 for value in element.values()])
        rel_score = round(abs_score / sub_size, 3)
        total_score += round(rel_score / size, 3)

    return total_score


def _elements(ls: list):
    size = len(ls)
    abs_score = sum([1 if (value or value == 0) else 0 for value in ls])
    return round(abs_score / size, 3)


def measure(ls: list):
    if not len(ls):
        raise ValueError('Cannot analyze empty list')
    t = type(ls[0])
    if t == dict:
        return _dicts(ls)
    if t == list:
        return round(sum([measure(sub_list) / len(ls) for sub_list in ls]), 3)
    if any([t == x for x in (int, float, str)]):
        return _elements(ls)
