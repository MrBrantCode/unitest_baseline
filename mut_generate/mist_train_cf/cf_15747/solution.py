"""
QUESTION:
Write a function named `modify_string` that takes a string as input, removes all spaces from the string, reverses the order of the characters, and converts all uppercase letters to lowercase.
"""

def modify_string(s):
    """
    This function takes a string as input, removes all spaces from the string, 
    reverses the order of the characters, and converts all uppercase letters to lowercase.

    Args:
        s (str): Input string

    Returns:
        str: Modified string
    """
    return s.replace(' ', '')[::-1].lower()