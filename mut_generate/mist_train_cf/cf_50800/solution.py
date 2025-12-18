"""
QUESTION:
Write a function named `sum_nested_dict_values` to find the sum of all integer values in a nested dictionary. The dictionary can have a maximum depth of 5 levels, with string keys and integer or dictionary values.
"""

def sum_nested_dict_values(nested_dict):
    total = 0
    for key, value in nested_dict.items():
        if isinstance(value, dict):
            total += sum_nested_dict_values(value)
        elif isinstance(value, int):
            total += value
    return total