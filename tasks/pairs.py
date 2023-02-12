from typing import Any

__all__ = (
    'corresponding_pairs',
)


def corresponding_pairs(arr1: list[Any], arr2: list[Any]) -> list[tuple[Any, Any]]:
    """
    Функция должна возвращать соответствующие элементы двух массивов:
    corresponding_pairs([1, 2], [3, 4]) == [(1, 3), (2, 4)]
    """
    if arr1 == [] or arr2 == []:
        return []
    res = []
    for i1, i2 in zip(arr1, arr2):
        res1 = [i1, i2]
        res.append(tuple(res1))
    return res
