"""
QUESTION:
Separate a string of alphanumeric characters into two parts. The function should take a string as input and return two strings, with the first string containing all the digits and the second string containing all the letters.
"""

def separate_string(s):
    """
    Separate a string of alphanumeric characters into two parts.
    
    Args:
    s (str): The input string containing alphanumeric characters.
    
    Returns:
    tuple: A tuple of two strings, with the first string containing all the digits and the second string containing all the letters.
    """
    left, right = '', ''
    for char in s:
        if char.isdigit():
            left += char
        else:
            right += char
    return left, right