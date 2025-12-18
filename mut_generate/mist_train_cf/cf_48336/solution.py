"""
QUESTION:
Write a function `filter_dict_by_key_start_char` that takes a dictionary `d` and a character `key_start_char` as inputs, and returns a new dictionary containing only the key-value pairs from `d` where the key starts with `key_start_char`. The function should be case-insensitive, and if no keys in `d` start with `key_start_char`, it should return a message indicating this. The function should also handle scenarios where `key_start_char` is not a single character.
"""

def filter_dict_by_key_start_char(d, key_start_char):
    """
    Returns a new dictionary containing only the key-value pairs from `d` 
    where the key starts with `key_start_char`. The function is case-insensitive.

    If no keys in `d` start with `key_start_char`, it returns a message indicating this.

    Args:
        d (dict): The input dictionary.
        key_start_char (str): The character to filter by.

    Returns:
        dict or str: A dictionary with filtered key-value pairs or a message if no keys match.
    """
    key_start_char = key_start_char.lower()
    filtered_dict = {k: v for k, v in d.items() if k[0].lower() == key_start_char}
    
    if filtered_dict:
        return filtered_dict
    else:
        return 'There are no keys in the dictionary that start with the specified letter.'