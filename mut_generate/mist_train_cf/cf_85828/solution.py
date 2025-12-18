"""
QUESTION:
Create a function named `filter_items` that takes a list of dictionaries and two parameters: an attribute and a value. The function should return a new list containing dictionaries from the original list where the specified attribute has a value greater than the given value. The function should handle cases where the attribute may not exist in all dictionaries.
"""

def filter_items(items, attr, value):
    return [item for item in items if attr in item and item[attr] > value]