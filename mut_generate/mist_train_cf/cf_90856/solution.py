"""
QUESTION:
Write a function `count_occurrences(lst, item)` that takes a list `lst` and an item as input, and returns the total number of occurrences of the item in the list, including occurrences within any nested lists or dictionaries.
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