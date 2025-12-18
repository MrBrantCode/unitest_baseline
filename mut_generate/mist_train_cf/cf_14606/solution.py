"""
QUESTION:
Write a function `unicode_character` that takes an integer as input and returns its corresponding Unicode character.
"""

def unicode_character(number):
    """
    This function takes an integer as input and returns its corresponding Unicode character.
    
    Parameters:
    number (int): The input integer.
    
    Returns:
    str: The Unicode character corresponding to the input integer.
    """
    return chr(number)