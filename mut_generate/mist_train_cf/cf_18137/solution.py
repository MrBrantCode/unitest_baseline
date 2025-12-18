"""
QUESTION:
Write a function `sort_dict_list` that takes a list of dictionaries and a key as input, and returns a new list sorted by the specified key using only lambda expressions and the built-in `sorted` function. The original list should remain unchanged.
"""

def sort_dict_list(dict_list, key):
    """
    Sorts a list of dictionaries based on a specific key value.

    Args:
        dict_list (list): A list of dictionaries.
        key (str): The key to sort by.

    Returns:
        list: A new sorted list of dictionaries.
    """
    return sorted(dict_list, key=lambda x: x[key])