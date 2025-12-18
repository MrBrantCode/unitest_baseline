"""
QUESTION:
Write a function named `monotonic` that takes a list of numbers `l` and an optional boolean parameter `strict` (defaulting to `False`) and returns `True` if the list is either monotonically increasing or decreasing, and `False` otherwise. If `strict` is `True`, the list must be strictly increasing or decreasing, meaning no two elements can be equal. If `strict` is `False`, the list can be non-strictly increasing or decreasing, allowing equal elements.
"""

def monotonic(l: list, strict: bool = False):
    if len(l) < 2:        
        return True

    diff = [l[i+1] - l[i] for i in range(len(l)-1)]

    if strict:
        return all(i > 0 for i in diff) or all(i < 0 for i in diff)
    else:
        return all(i >= 0 for i in diff) or all(i <= 0 for i in diff)