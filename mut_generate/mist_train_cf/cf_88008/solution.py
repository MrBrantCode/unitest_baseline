"""
QUESTION:
Write a function `sum_nested_dict_values` that takes a nested dictionary as input, where the dictionary may contain integers, lists, sets, and tuples as values. The function should return the sum of all values in the dictionary, with the following conditions:

- If a value is an integer, add it to the sum.
- If a value is a tuple, square each element and add the squared values to the sum.
- If a value is a list or a set, square each element, remove duplicates, and add the unique squared values to the sum.

The function should recursively handle nested dictionaries.
"""

def sum_nested_dict_values(nested_dict):
    total_sum = 0

    for key, value in nested_dict.items():
        if isinstance(value, dict):
            total_sum += sum_nested_dict_values(value)
        elif isinstance(value, int):
            total_sum += value
        elif isinstance(value, tuple):
            total_sum += sum(num ** 2 for num in value)
        elif isinstance(value, list) or isinstance(value, set):
            unique_squared_values = set(num ** 2 for num in value)
            total_sum += sum(unique_squared_values)

    return total_sum