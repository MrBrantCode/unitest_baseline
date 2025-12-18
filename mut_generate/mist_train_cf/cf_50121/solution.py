"""
QUESTION:
Write a function `sort_dict_by_value` that sorts a dictionary by its values. The function should take a dictionary as input and return a new dictionary (or a list of tuples if a dictionary is not possible) with the same key-value pairs, but sorted by the values. The function should also have an optional parameter to specify whether the sorting should be in ascending or descending order.
"""

def sort_dict_by_value(dictionary, reverse=False):
    """
    Sorts a dictionary by its values.

    Args:
    dictionary (dict): The dictionary to be sorted.
    reverse (bool): Optional parameter to specify whether the sorting should be in ascending or descending order.

    Returns:
    dict or list: A new dictionary (or a list of tuples if a dictionary is not possible) with the same key-value pairs, but sorted by the values.
    """
    return dict(sorted(dictionary.items(), key = lambda x: x[1], reverse=reverse))