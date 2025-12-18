"""
QUESTION:
Write a function `check_string` that takes a string as input and returns the count of uppercase characters and a list of positions of special characters in the string. The function should consider alphabets and numbers as non-special characters, and all other characters as special characters. The position of characters in the string is 0-indexed.
"""

def check_string(s):
    """
    This function takes a string as input, returns the count of uppercase characters 
    and a list of positions of special characters in the string.

    Parameters:
    s (str): The input string.

    Returns:
    tuple: A tuple containing the count of uppercase characters and a list of 
    positions of special characters.

    """
    uppercase_count = sum(1 for c in s if c.isupper())
    special_chars_pos = [i for i, c in enumerate(s) if not c.isalnum()]
    
    return uppercase_count, special_chars_pos