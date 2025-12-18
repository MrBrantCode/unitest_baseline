"""
QUESTION:
Write a function `sort_dicts_by_value(b)` that takes a list of dictionaries `b` as input, where each dictionary contains a single key-value pair with a lowercase letter as the key and an integer as the value. The function should sort the list of dictionaries in ascending order based on the integer values and return the sorted list.
"""

def sort_dicts_by_value(b):
    return sorted(b, key=lambda x: list(x.values())[0])