"""
QUESTION:
Write a function named `count_occurrence` that takes two parameters: `item` and `data`. The function should count the occurrence of `item` in `data`, handling cases where `item` is a nested list or dictionary, and ignoring nested lists or dictionaries that are contained within another nested list or dictionary. The function should be able to handle `item` as a nested data structure of any depth and mixed types, and correctly count each occurrence. The function should also handle cases where `item` is a tuple, set, or any other data structure that can contain elements.

Restrictions: `item` can be any data type, and `data` can be a list or a dictionary. The function should recursively search for `item` in `data`.
"""

def count_occurrence(item, data):
    count = 0
    if isinstance(data, list):
        for elem in data:
            if elem == item:
                count += 1
            elif isinstance(elem, (list, dict)):
                count += count_occurrence(item, elem)
    elif isinstance(data, dict):
        for value in data.values():
            if value == item:
                count += 1
            elif isinstance(value, (list, dict)):
                count += count_occurrence(item, value)
    return count