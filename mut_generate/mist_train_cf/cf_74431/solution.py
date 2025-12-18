"""
QUESTION:
Write a function `is_inherent(string1, string2)` that checks if `string2` is a substring of `string1`, meaning it contains the same sequence of characters in the same order. The function should return `True` if `string2` is a substring of `string1`, and `False` otherwise. The input strings will only contain characters.
"""

def is_inherent(string1, string2):
    """
    Checks if string2 is a substring of string1.

    Args:
        string1 (str): The main string to be checked.
        string2 (str): The substring to be searched in string1.

    Returns:
        bool: True if string2 is a substring of string1, False otherwise.
    """
    return string2 in string1