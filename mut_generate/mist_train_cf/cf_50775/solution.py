"""
QUESTION:
Write a function `sum_nested_dict_values` that calculates the sum of all numerical values in a nested dictionary, including integers and floating point numbers. The function should recursively traverse the dictionary, ignoring non-numeric values.
"""

def sum_nested_dict_values(d):
    total = 0
    for k, v in d.items():
        if type(v) is dict:
            total += sum_nested_dict_values(v)
        else:
            try:
                total += float(v)
            except (TypeError, ValueError):
                continue
    return total