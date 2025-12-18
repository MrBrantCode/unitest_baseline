"""
QUESTION:
Create a function `sort_dict_list` that sorts a list of dictionaries based on a specific key value using a lambda expression. The function should take two parameters: `dict_list` (a list of dictionaries) and `key` (the key to sort by). The function should return the sorted list of dictionaries. The function should be able to handle lists of dictionaries with any keys and any number of key-value pairs.
"""

def sort_dict_list(dict_list, key):
    """
    Sorts a list of dictionaries based on a specific key value.

    Args:
        dict_list (list): A list of dictionaries.
        key (str): The key to sort by.

    Returns:
        list: The sorted list of dictionaries.
    """
    return sorted(dict_list, key=lambda x: x[key])