"""
QUESTION:
Write a function `retrieve_last_char` that takes a string `s` as input and returns the last character of the string. If the input string is empty, the function should return an empty string.
"""

def retrieve_last_char(s):
    """
    This function retrieves the last character of a given string.
    
    Args:
        s (str): The input string.
    
    Returns:
        str: The last character of the string. If the string is empty, an empty string is returned.
    """
    return s[-1] if s else ""