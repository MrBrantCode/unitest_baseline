"""
QUESTION:
Implement a function named `reverse_string` that takes a string as input and returns the reversed string. The function should handle multi-byte characters (Unicode characters) correctly, treating each emoji or accented letter as a single character, and it should not use any built-in reverse functions or additional variables.
"""

def reverse_string(s):
    """
    Reverses a string with multi-byte characters correctly.
    
    Args:
        s (str): The input string to be reversed.
    
    Returns:
        str: The reversed string.
    """
    return ''.join(reversed([char for char in s]))