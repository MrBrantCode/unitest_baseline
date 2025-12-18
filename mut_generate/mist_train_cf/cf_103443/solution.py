"""
QUESTION:
Create a function named `remove_parentheses` that takes a string as input and returns the string with all pairs of parentheses and the words inside them removed. The function should be able to handle strings with nested parentheses.
"""

import re

def remove_parentheses(s):
    """
    This function takes a string as input and returns the string with all pairs of parentheses and the words inside them removed.

    Parameters:
    s (str): The input string.

    Returns:
    str: The string with all pairs of parentheses and the words inside them removed.
    """
    return re.sub(r'\([^)]*\)', '', s)