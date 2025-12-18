"""
QUESTION:
Write a function named `merge_dicts` that takes two dictionaries `dict1` and `dict2` as input and returns a new dictionary that combines `dict1` and `dict2`, excluding any keys from `dict2` that already exist in `dict1`, while maintaining the original order of keys from both dictionaries. The function should be compatible with Python 3.7 and above, where dictionary insertion order is preserved.
"""

def merge_dicts(dict1, dict2):
    """
    Merge two dictionaries, excluding any keys from dict2 that already exist in dict1, 
    while maintaining the original order of keys from both dictionaries.
    
    Args:
        dict1 (dict): The primary dictionary.
        dict2 (dict): The secondary dictionary.
    
    Returns:
        dict: A new dictionary that combines dict1 and dict2.
    """
    return {**dict1, **{k: v for k, v in dict2.items() if k not in dict1}}