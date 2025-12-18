"""
QUESTION:
Write a function named `last_uppercase_character` that retrieves the last character of a given string and returns it in uppercase. The input string will not be empty.
"""

def last_uppercase_character(s):
    """
    Retrieves the last character of a given string and returns it in uppercase.

    Args:
    s (str): The input string.

    Returns:
    str: The last character of the input string in uppercase.
    """
    return s[-1].upper()