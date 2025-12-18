"""
QUESTION:
Write a Python function `reorder_dict` that takes a dictionary as input, sorts it by its values in ascending order, and returns the sorted dictionary. If there are multiple items with the same value, ensure that their order is consistent.
"""

def reorder_dict(my_dict):
    # this will sort the dictionary by its values
    sort_dict = {k: v for k, v in sorted(my_dict.items(), key=lambda item: item[1])}
    return sort_dict