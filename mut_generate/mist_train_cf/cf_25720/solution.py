"""
QUESTION:
Write a function called `remove_spaces` that takes a string as input and returns the string with all blank spaces removed. The function should not use any external libraries.
"""

def remove_spaces(s):
    """
    Removes all blank spaces from a given string.
    
    Args:
        s (str): The input string.
    
    Returns:
        str: The string with all blank spaces removed.
    """
    return s.replace(" ", "")