"""
QUESTION:
Write a function `count_occurrences` that takes a list (which can contain nested lists or dictionaries) and an item as input, and returns the total count of occurrences of the item in the list and its nested structures. The function should recursively count occurrences in lists and dictionaries, and handle cases where the item is a value in a dictionary or an element in a list.
"""

def count_occurrences(lst, item):
    count = 0
    if isinstance(lst, list):
        for element in lst:
            if element == item:
                count += 1
            elif isinstance(element, (list, dict)):
                count += count_occurrences(element, item)
    elif isinstance(lst, dict):
        for key, value in lst.items():
            if key == item or value == item:
                count += 1
            elif isinstance(value, (list, dict)):
                count += count_occurrences(value, item)
    return count