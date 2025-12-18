"""
QUESTION:
Write a function called `reverse_string` that takes a string as input and returns the reversed string. The function should have a time complexity of O(n), where n is the length of the input string.
"""

def reverse_string(s):
    """
    Reverses a given string.
    
    Time complexity: O(n), where n is the length of the input string.
    
    Parameters:
    s (str): The input string to be reversed.
    
    Returns:
    str: The reversed string.
    """
    return s[::-1]