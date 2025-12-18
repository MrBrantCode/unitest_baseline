"""
QUESTION:
Write a function named `sum_nested_dict` that calculates the sum of all integers in a given nested dictionary. The dictionary can contain other dictionaries as values with a depth of up to 10 levels, and may also contain lists with integers and dictionaries. The function must handle cases where the dictionary contains circular references. The input dictionary is expected to have string keys and values that are either integers, dictionaries, or lists of integers and dictionaries.
"""

def sum_nested_dict(d, seen=None):
    if seen is None:
        seen = set()

    if id(d) in seen:
        return 0
    seen.add(id(d))

    total = 0
    for value in d.values():
        if isinstance(value, int):
            total += value
        elif isinstance(value, dict):
            total += sum_nested_dict(value, seen)
        elif isinstance(value, list):
            for item in value:
                if isinstance(item, int):
                    total += item
                elif isinstance(item, dict):
                    total += sum_nested_dict(item, seen)
    return total