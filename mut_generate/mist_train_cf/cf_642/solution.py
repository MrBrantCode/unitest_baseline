"""
QUESTION:
Write a function named `count_occurrence` that takes two parameters: `item` and `data`. The function should count the occurrence of `item` in `data`, which can be a list or a dictionary, handling cases where `item` is a nested list or dictionary and ignoring any nested lists or dictionaries that are contained within another nested list or dictionary. The function should handle cases where `item` is a tuple, set, or any other data structure that can contain elements, and it should handle cases where `item` is a nested data structure of any depth, mixed types, and with duplicates. The function should return the total count of occurrences of `item` in `data`.
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