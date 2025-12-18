"""
QUESTION:
Write a function `check_key_exists` that takes two parameters, `nested_dict` and `key`, to check if a given key exists in a nested dictionary or not. The key may be a nested key separated by dots.
"""

def check_key_exists(nested_dict, key):
    """
    Checks if a given key exists in a nested dictionary or not.
    
    The key may be a nested key separated by dots.
    
    Args:
    nested_dict (dict): The dictionary to search in.
    key (str): The key to search for.
    
    Returns:
    bool: True if the key exists, False otherwise.
    """
    keys = key.split(".")
    current_dict = nested_dict

    for key in keys:
        if key in current_dict:
            current_dict = current_dict[key]
        else:
            return False
    return True