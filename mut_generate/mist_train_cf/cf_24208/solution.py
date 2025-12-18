"""
QUESTION:
Write a function called `merge_dictionaries` to combine two given dictionaries into one. If there are common keys, the values from the second dictionary should be used. The function should take two dictionaries as input and return the merged dictionary.
"""

def merge_dictionaries(dict1, dict2):
    """
    Merge two dictionaries into one. If there are common keys, 
    the values from the second dictionary are used.

    Args:
        dict1 (dict): The first dictionary.
        dict2 (dict): The second dictionary.

    Returns:
        dict: The merged dictionary.
    """
    return {**dict1, **dict2}