"""
QUESTION:
Create a function `merge_dicts` that takes two dictionaries `dict1` and `dict2` as input and returns a new dictionary. The returned dictionary should contain key-value pairs from both `dict1` and `dict2` where the key is a string and the value is a positive integer that is divisible by 3. Any key-value pairs in either `dict1` or `dict2` that do not meet this requirement should be skipped.
"""

def merge_dicts(dict1, dict2):
    """
    This function merges two dictionaries and filters out key-value pairs where the key is not a string or the value is not a positive integer divisible by 3.

    Args:
        dict1 (dict): The first dictionary to merge.
        dict2 (dict): The second dictionary to merge.

    Returns:
        dict: A new dictionary containing key-value pairs from both input dictionaries that meet the requirements.
    """
    merged_dict = {}

    for key, value in dict1.items():
        if isinstance(key, str) and isinstance(value, int) and value > 0 and value % 3 == 0:
            merged_dict[key] = value

    for key, value in dict2.items():
        if isinstance(key, str) and isinstance(value, int) and value > 0 and value % 3 == 0:
            merged_dict[key] = value

    return merged_dict