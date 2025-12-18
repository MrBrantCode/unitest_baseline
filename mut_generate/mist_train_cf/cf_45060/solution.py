"""
QUESTION:
Write a function named `all_empty` that takes a list as input and returns `True` if the list and all its nested lists are empty. The function should handle circular references without entering an infinite loop. The function should return `False` if any non-list element is found in the input list or its nested lists.
"""

def all_empty(lst, seen=None):
    if seen is None:
        seen = set()
    if id(lst) in seen:
        return True
    seen.add(id(lst))
    for item in lst:
        if isinstance(item, list):
            if not all_empty(item, seen):
                return False
        else:
            return False
    return True