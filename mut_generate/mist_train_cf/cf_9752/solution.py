"""
QUESTION:
Create a function `get_odd_unicode_chars` that takes a string as input and returns an array of Unicode objects containing only characters with odd Unicode values.
"""

def get_odd_unicode_chars(s):
    """
    Returns an array of Unicode objects containing only characters with odd Unicode values.

    Args:
        s (str): The input string.

    Returns:
        list: A list of characters with odd Unicode values.
    """
    return [char for char in s if ord(char) % 2 != 0]