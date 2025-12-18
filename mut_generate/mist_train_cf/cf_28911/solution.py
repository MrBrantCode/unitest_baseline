"""
QUESTION:
Implement a function `author_set` that takes a boolean parameter `sort` (defaulting to `True`) and a variable number of keyword arguments. The function should return a list of unique values obtained from the keyword arguments. If `sort` is `True`, the list should be sorted in ascending order. Any non-iterable keyword argument values should be ignored, and a `TypeError` should not be raised.
"""

def author_set(sort=True, **kwargs):
    values = []
    for arg in kwargs.values():
        try:
            values.extend(arg)
        except TypeError:
            pass
    unique_values = list(set(values))
    return sorted(unique_values) if sort else unique_values