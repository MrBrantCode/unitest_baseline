"""
QUESTION:
Write a function named `get_fifth_letter` that takes a string as input and returns the fifth letter of the string. If the string has less than five letters, return the string "Error: The string should have at least five letters."
"""

def get_fifth_letter(s):
    """
    Returns the fifth letter of the input string.
    
    If the string has less than five letters, returns an error message.

    Args:
        s (str): The input string.

    Returns:
        str: The fifth letter of the string or an error message.
    """
    if len(s) < 5:
        return "Error: The string should have at least five letters."
    else:
        return s[4]