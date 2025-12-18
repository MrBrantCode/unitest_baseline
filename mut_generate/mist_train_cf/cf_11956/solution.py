"""
QUESTION:
Write a function `invert_dict` that inverts a given dictionary, excluding any keys that contain the letter 'a'. The function should take a dictionary as input and return a new dictionary where keys and values are swapped, but only for key-value pairs where the key does not contain 'a'.
"""

def invert_dict(input_dict):
    """
    Inverts a given dictionary, excluding any keys that contain the letter 'a'.

    Args:
        input_dict (dict): The dictionary to be inverted.

    Returns:
        dict: A new dictionary where keys and values are swapped, but only for key-value pairs where the key does not contain 'a'.
    """
    return {v: k for k, v in input_dict.items() if 'a' not in k}