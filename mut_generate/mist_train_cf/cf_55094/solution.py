"""
QUESTION:
Write a function named `max_unique_substrings` that calculates the maximum number of unique sub-strings that can be created from a given string. The function should take a string as input and return the maximum number of unique sub-strings. The input string will only contain alphabetic characters.
"""

def max_unique_substrings(s):
    """
    Calculate the maximum number of unique sub-strings that can be created from a given string.
    
    Args:
    s (str): The input string containing alphabetic characters.
    
    Returns:
    int: The maximum number of unique sub-strings.
    """
    n = len(s)
    return n * (n + 1) // 2