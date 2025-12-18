"""
QUESTION:
Write a Python function named `sort_dict_list` that takes two parameters: a list of dictionaries (`dict_list`) and a specific key (`key`). The function should sort the list of dictionaries in ascending order based on the values of the specified key and return the sorted list. The function should also have the ability to sort the list in descending order if an optional parameter `reverse` is set to `True` (default is `False`).
"""

def sort_dict_list(dict_list, key, reverse=False):
    """
    Sorts the list of dictionaries in ascending order based on the values of the specified key.

    Args:
        dict_list (list): A list of dictionaries.
        key (str): The key to sort by.
        reverse (bool, optional): Sort in descending order if True. Defaults to False.

    Returns:
        list: The sorted list of dictionaries.
    """
    return sorted(dict_list, key=lambda x: x[key], reverse=reverse)