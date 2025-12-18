"""
QUESTION:
Write a Python function named `merge_dictionaries` that takes two dictionaries, `dict1` and `dict2`, as input and returns a new dictionary containing all key-value pairs from both input dictionaries. The function should not modify the original dictionaries and should handle cases where the dictionaries have unique keys.
"""

def merge_dictionaries(dict1, dict2):
    """
    Merge two dictionaries into a new dictionary.

    Args:
        dict1 (dict): The first dictionary.
        dict2 (dict): The second dictionary.

    Returns:
        dict: A new dictionary containing all key-value pairs from both input dictionaries.
    """
    merged_dict = dict1.copy()
    merged_dict.update(dict2)
    return merged_dict