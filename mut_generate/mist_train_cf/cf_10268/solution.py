"""
QUESTION:
Create a function `replace_chars` that takes a string as input and returns a new string where every occurrence of 'a' is replaced with 'A' and every occurrence of 'e' is replaced with 'E'. The function should handle any input string.
"""

def replace_chars(s):
    """
    This function replaces every occurrence of 'a' with 'A' and every occurrence of 'e' with 'E' in a given string.

    Args:
        s (str): The input string.

    Returns:
        str: The modified string.
    """
    return s.replace('a', 'A').replace('e', 'E')