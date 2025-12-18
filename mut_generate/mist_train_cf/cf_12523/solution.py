"""
QUESTION:
Write a function called `count_pattern` to count the number of times a given pattern has occurred in a given string. The function should be case-sensitive and support special characters in the pattern.
"""

def count_pattern(text, pattern):
    """
    Count the number of times a given pattern has occurred in a given string.
    
    This function is case-sensitive and supports special characters in the pattern.
    
    Parameters:
    text (str): The string to search for the pattern.
    pattern (str): The pattern to search for in the text.
    
    Returns:
    int: The number of times the pattern occurs in the text.
    """
    return text.count(pattern)