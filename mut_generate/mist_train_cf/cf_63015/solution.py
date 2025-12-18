"""
QUESTION:
Write a function named `monotonic` that takes a list of elements and an optional boolean parameter `strict` (defaulting to `False`). The function should return `True` if the list elements are either monotonically increasing or decreasing, considering the `strict` parameter. If `strict` is `True`, the function should ignore adjacent equal elements and consider the list monotonic if the remaining elements are either monotonically increasing or decreasing. If `strict` is `False`, the function should consider the list monotonic if the elements are either monotonically increasing or decreasing, allowing for adjacent equal elements.
"""

def is_monotonic(lst, strict=False):
    if len(lst) < 2:
        return True

    if strict:
        lst = [x for i, x in enumerate(lst) if i == 0 or x != lst[i - 1]]

    increasing = all(lst[i] <= lst[i + 1] for i in range(len(lst) - 1))
    decreasing = all(lst[i] >= lst[i + 1] for i in range(len(lst) - 1))

    return increasing or decreasing