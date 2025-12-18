"""
QUESTION:
Create a function called `common_unique` that takes two lists `l1` and `l2` as inputs, and returns a list containing only distinct elements common to both lists, sorted in ascending order. The function should be able to handle various data types, including integers, floats, and strings.
"""

def common_unique(l1: list, l2: list):
    """Returns sorted unique elements common in both lists."""
    # Identifying common, unique items
    common = set(l1) & set(l2)
    return sorted(list(common))