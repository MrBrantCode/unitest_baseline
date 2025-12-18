"""
QUESTION:
Create a function named `is_unique_list` that checks if all items in a list are unique. The list may contain nested lists and/or dictionaries. The function should not use any built-in functions or data structures to check for uniqueness.
"""

def is_unique_list(lst):
    seen = []
    for item in lst:
        if isinstance(item, list):
            if not is_unique_list(item):
                return False
        elif isinstance(item, dict):
            if list(item.keys()) != sorted(list(set(item.keys()))) or not is_unique_list(list(item.values())):
                return False
        elif item in seen:
            return False
        seen.append(item)
    return True