"""
QUESTION:
Write a Python function named `sort_dictionaries` that takes a list of dictionaries as input and returns the sorted list based on a specified key. The function should prioritize computational efficiency and code readability. The input list contains dictionaries with the same structure and the specified key exists in each dictionary.
"""

def sort_dictionaries(dictionaries, key):
    """
    Sorts a list of dictionaries based on a specified key.

    Args:
    dictionaries (list): A list of dictionaries.
    key (str): The key to sort by.

    Returns:
    list: The sorted list of dictionaries.
    """
    return sorted(dictionaries, key=lambda d: d[key])