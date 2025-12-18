"""
QUESTION:
Write a function `sort_values` that sorts a given set of values, prioritizing integers over other data types. The function should return a list where all integers are sorted in ascending order and appear before other data types, which should also be sorted in ascending order. The function should work with a set of mixed data types, including integers, floats, strings, and other types.
"""

def sort_values(values):
    int_values = sorted([v for v in values if isinstance(v, int)])
    other_values = sorted([v for v in values if not isinstance(v, int)])
    return int_values + other_values