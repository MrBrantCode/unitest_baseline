"""
QUESTION:
Write a function `sort_dicts_by_key` that takes in three arguments: a list of dictionaries `dicts`, a string `key` representing the key to sort by, and a boolean `descending` indicating whether the sorting should be in descending order. The function should return a new list of dictionaries sorted by the values associated with the specified key. If `descending` is `True`, the sorting should be in descending order, otherwise it should be in ascending order. The dictionaries in the list should have the same keys, but the values may be of different data types.
"""

def sort_dicts_by_key(dicts, key, descending=False):
    """
    Sort a list of dictionaries based on a specific key.
    Args:
        dicts (list): A list of dictionaries with the same keys.
        key (str): The key to sort by.
        descending (bool): If True, sort in descending order.
    Returns:
        A new list of dictionaries sorted by the values of the specified key.
    """
    return sorted(dicts, key=lambda x: x[key], reverse=descending)