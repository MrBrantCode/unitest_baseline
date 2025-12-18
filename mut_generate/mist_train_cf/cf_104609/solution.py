"""
QUESTION:
Create a function `filter_strings` that takes a list of strings as input. The function should return a new list containing only the strings that contain the letter 'a' and end with the letter 'e'.
"""

def filter_strings(strings):
    """
    This function filters a list of strings and returns a new list containing only the strings 
    that contain the letter 'a' and end with the letter 'e'.

    Args:
        strings (list): A list of strings.

    Returns:
        list: A list of filtered strings.
    """
    return [string for string in strings if 'a' in string and string.endswith('e')]