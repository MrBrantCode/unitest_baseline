"""
QUESTION:
Write a function `monotonic(l: list, k: int, strict: bool = False)` that returns `True` if the difference between every two adjacent elements in the list `l` is `k`, considering the `strict` parameter. If `strict` is `True`, no two adjacent elements can be equal; otherwise, they can be.
"""

def monotonic(l: list, k: int, strict: bool = False):
    if strict:
        return all(x-y == k for x, y in zip(l[1:], l[:-1]))
    else:
        return all(x-y == k for x, y in zip(l[1:], l[:-1])) or all(x-y == 0 for x, y in zip(l[1:], l[:-1]))