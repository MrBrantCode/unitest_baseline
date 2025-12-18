"""
QUESTION:
Write a function named `merge_dicts` that takes two dictionaries as input and returns a new dictionary. The new dictionary should only contain key-value pairs where the key is a string and the value is a positive integer. Key-value pairs in either dictionary that do not meet this requirement should be skipped.
"""

def merge_dicts(dict1, dict2):
    """
    Merge two dictionaries into a new dictionary. 
    The new dictionary contains key-value pairs where the key is a string and the value is a positive integer.
    
    Parameters:
    dict1 (dict): The first dictionary.
    dict2 (dict): The second dictionary.
    
    Returns:
    dict: A new dictionary containing key-value pairs where the key is a string and the value is a positive integer.
    """
    merged_dict = {}
    for key, value in dict1.items():
        if isinstance(key, str) and isinstance(value, int) and value > 0:
            merged_dict[key] = value
    for key, value in dict2.items():
        if isinstance(key, str) and isinstance(value, int) and value > 0:
            merged_dict[key] = value
    return merged_dict