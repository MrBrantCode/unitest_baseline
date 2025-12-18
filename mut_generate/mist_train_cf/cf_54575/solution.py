"""
QUESTION:
Write a function `sum_nested_dict` that calculates the sum of all integer values in a given nested dictionary. The dictionary can contain other dictionaries, lists, and integers. The function should recursively handle these complexities to return the total sum of all integer values.
"""

def sum_nested_dict(d):
    total = 0
    for k, v in d.items():
        if isinstance(v, dict):
            total += sum_nested_dict(v)
        elif isinstance(v, list):
            total += sum(i if isinstance(i, int) else sum_nested_dict(i) for i in v)
        elif isinstance(v, int):
            total += v
    return total