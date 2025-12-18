"""
QUESTION:
Write a function named `invert_dict` that takes a dictionary as input, inverts its key-value pairs, and returns the resulting dictionary. The inverted dictionary should exclude any original keys that contain the letter 'a' and only include new keys that have a length greater than 2. If multiple original keys map to the same value, the resulting dictionary should map the value to a list of those keys.
"""

def invert_dict(input_dict):
    """
    Inverts a dictionary's key-value pairs, excluding keys with 'a' and new keys with length <= 2.
    If multiple keys map to the same value, the new key maps to a list of those keys.

    Args:
    input_dict (dict): The dictionary to be inverted.

    Returns:
    dict: The inverted dictionary.
    """
    inverted_dict = {}
    for key, value in input_dict.items():
        if 'a' not in key:
            if isinstance(value, str) and len(value) > 2:
                if value in inverted_dict:
                    if not isinstance(inverted_dict[value], list):
                        inverted_dict[value] = [inverted_dict[value]]
                    inverted_dict[value].append(key)
                else:
                    inverted_dict[value] = key
    return inverted_dict