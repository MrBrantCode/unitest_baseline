"""
QUESTION:
Write a function `get_third_char` that retrieves the third character from a given string using its index, but only if the string length is greater than 5. The function should return the third character if the condition is met, otherwise it should return a message or handle the situation accordingly.
"""

def get_third_char(s):
    """
    Retrieves the third character from a given string using its index.

    Args:
    s (str): The input string.

    Returns:
    str: The third character of the string if its length is greater than 5, otherwise None.
    """
    if len(s) > 5:
        return s[2]
    else:
        return None