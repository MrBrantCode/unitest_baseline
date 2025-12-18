"""
QUESTION:
Write a function named `uppercase_last_character` that takes a string as input and returns the last character of the string converted to uppercase.
"""

def uppercase_last_character(s):
    """
    Returns the last character of the input string converted to uppercase.

    Args:
        s (str): The input string.

    Returns:
        str: The last character of the input string in uppercase.
    """
    if not s:  # Check for empty string
        return ""
    return s[-1].upper()