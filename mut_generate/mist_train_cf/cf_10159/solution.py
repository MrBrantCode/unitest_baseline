"""
QUESTION:
Write a function `compare_dictionaries` that compares two dictionaries for equality, considering only the key-value pairs, and ignoring their order. The function should return `True` if the dictionaries are equal, and `False` otherwise. The input dictionaries can contain any number of key-value pairs, and the keys can be of any hashable type.
"""

def compare_dictionaries(dict1, dict2):
    """
    Compare two dictionaries for equality, considering only the key-value pairs, and ignoring their order.

    Args:
        dict1 (dict): The first dictionary to compare.
        dict2 (dict): The second dictionary to compare.

    Returns:
        bool: True if the dictionaries are equal, False otherwise.
    """
    return dict1 == dict2