"""
QUESTION:
Create a function named `get_ascii_codes` that takes a string as input and returns a list of ASCII codes for each character in the string. The function should work for strings consisting of single words and multiple words.
"""

def get_ascii_codes(s):
    """
    This function takes a string as input and returns a list of ASCII codes for each character in the string.
    
    Args:
        s (str): The input string.
    
    Returns:
        list: A list of ASCII codes for each character in the string.
    """
    return [ord(c) for c in s]