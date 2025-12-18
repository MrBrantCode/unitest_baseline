"""
QUESTION:
Write a function named `sort_dict_list_by_key` that takes a list of dictionaries and a key as input, and returns a new list with the dictionaries sorted by the specified key using only lambda expressions and the built-in `sorted()` function. The original list should remain unchanged.
"""

def sort_dict_list_by_key(dict_list, key):
    """Sorts a list of dictionaries by a specified key using lambda expressions."""
    return sorted(dict_list, key=lambda x: x[key])