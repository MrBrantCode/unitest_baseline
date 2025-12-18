"""
QUESTION:
Create a function `sort_dict_list` that sorts a list of dictionaries based on a specific key value using only lambda expressions. The function should be able to handle cases where the key value is a nested attribute within the dictionaries. The function takes two parameters: `dict_list` (the list of dictionaries) and `key_path` (the key value or nested key path to sort by). The function should return the sorted list of dictionaries.

Example inputs:
- `dict_list`: a list of dictionaries where each dictionary contains a key or nested key path to sort by.
- `key_path`: a string representing the key value or nested key path to sort by (e.g., `'age'` or `'address.city'`).
"""

def sort_dict_list(dict_list, key_path):
    """
    Sorts a list of dictionaries based on a specific key value or nested key path.

    Args:
        dict_list (list): A list of dictionaries.
        key_path (str): A string representing the key value or nested key path to sort by.

    Returns:
        list: The sorted list of dictionaries.
    """
    keys = key_path.split('.')
    return sorted(dict_list, key=lambda x: nested_get(x, keys))


def nested_get(d, keys):
    """
    Retrieves a nested value from a dictionary.

    Args:
        d (dict): The dictionary to retrieve the value from.
        keys (list): A list of keys to access the nested value.

    Returns:
        The nested value.
    """
    for key in keys:
        if isinstance(d, dict) and key in d:
            d = d[key]
        else:
            return None
    return d