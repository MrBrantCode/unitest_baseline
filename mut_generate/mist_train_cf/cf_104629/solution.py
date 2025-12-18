"""
QUESTION:
Write a function `find_max_length_key` that takes a dictionary as input and returns the key with the maximum length string value. In case of multiple keys with the same maximum length value, return the first key encountered. The function should only consider string values and ignore non-string values.
"""

def find_max_length_key(dictionary):
    """
    This function finds the key with the maximum length string value in a dictionary.

    Args:
    dictionary (dict): The input dictionary.

    Returns:
    str: The key with the maximum length string value.
    """
    max_length = 0
    max_key = ''
    max_value = ''

    for key, value in dictionary.items():
        if isinstance(value, str) and len(value) > max_length:
            max_length = len(value)
            max_key = key
            max_value = value

    return max_key