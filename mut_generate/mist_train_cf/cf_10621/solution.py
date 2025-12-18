"""
QUESTION:
Write a function `capitalize_string` that takes a string as input, capitalizes the first letter of each word while keeping the rest of the letters lowercase, and returns the formatted string.
"""

def capitalize_string(s):
    """
    Capitalizes the first letter of each word in a string while keeping the rest of the letters lowercase.

    Args:
        s (str): The input string.

    Returns:
        str: The formatted string.
    """
    return s.title()