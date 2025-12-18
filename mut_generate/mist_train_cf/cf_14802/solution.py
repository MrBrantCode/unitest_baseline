"""
QUESTION:
Write a function named `convert_to_number` that takes a string of characters as input and returns the integer represented by the string after removing all non-digit characters.
"""

def convert_to_number(s):
    """
    This function takes a string of characters as input, removes all non-digit characters, 
    and returns the integer represented by the resulting string.
    
    Parameters:
    s (str): The input string containing a mix of digits and non-digit characters.
    
    Returns:
    int: The integer represented by the string after removing all non-digit characters.
    """
    return int(''.join(filter(str.isdigit, s)))