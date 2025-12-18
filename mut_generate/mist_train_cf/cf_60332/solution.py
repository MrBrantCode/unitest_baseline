"""
QUESTION:
Implement a function `is_dict_empty(d)` that checks if a dictionary `d` is empty and also verifies that any nested dictionaries within `d` are empty. The function should return `True` only if the primary dictionary and all nested dictionaries are empty.
"""

def is_dict_empty(d):
    """
    Checks if a dictionary and its nested dictionaries are empty.

    Args:
    d (dict): The dictionary to check.

    Returns:
    bool: True if the dictionary and its nested dictionaries are empty, False otherwise.
    """
    if not isinstance(d, dict) or d:  
        return False
    for v in d.values():
        if isinstance(v, dict):
            if not is_dict_empty(v):  
                return False
    return True