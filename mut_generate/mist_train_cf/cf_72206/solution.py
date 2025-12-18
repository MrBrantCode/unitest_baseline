"""
QUESTION:
Implement a function `f` that takes a list `x` (which may contain nested lists) and a boolean parameter `reverse` (defaulting to `False`) as input, and returns a sorted list of integers. The list should be sorted in ascending order if `reverse` is `False`, and in descending order if `reverse` is `True`. The function should be able to handle nested lists by flattening them before sorting.
"""

def flatten(lst):
    """Flattens a nested list"""
    flat_list = []
    for i in lst:
        if isinstance(i, list):
            flat_list.extend(flatten(i))
        else:
            flat_list.append(i)
    return flat_list

def f(x, reverse=False):
    """Sorts a list in ascending or descending order"""
    x = flatten(x)
    return sorted(x, reverse=reverse)