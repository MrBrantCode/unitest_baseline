"""
QUESTION:
Create a function named `monotonic` that accepts a list (`l`) and an optional boolean parameter (`strict` with a default value of `False`). The function should return `True` if all elements in the list (or sub-lists, in the case of nested lists) are monotonically increasing or decreasing, taking into account the `strict` requirement. The function should support both 1D and 2D lists.
"""

def monotonic(l: list, strict: bool = False):
    try:
        is_nested = any(isinstance(i, list) for i in l)
    except TypeError:
        return False

    if is_nested:
        return all(monotonic(sub_list, strict) for sub_list in l)     # recursion
    else:
        if strict:
            return all(i < j for i, j in zip(l, l[1:])) or all(i > j for i, j in zip(l, l[1:]))
        else:
            return all(i <= j for i, j in zip(l, l[1:])) or all(i >= j for i, j in zip(l, l[1:]))