"""
QUESTION:
Create a function `remove_element` that takes two parameters: an integer `target_int` and a list `list_val`, which can contain elements of different data types and nested lists. The function should recursively remove all occurrences of `target_int` from `list_val`, preserving the original list structure and other data types. The function should be optimized for performance to handle larger lists efficiently.
"""

def remove_element(target_int, list_val):
    new_list = []
    for i in list_val:
        if isinstance(i, list):
            new_list.append(remove_element(target_int, i))
        elif not isinstance(i, int) or i != target_int:
            new_list.append(i)
    return new_list