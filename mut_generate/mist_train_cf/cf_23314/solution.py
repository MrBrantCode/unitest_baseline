"""
QUESTION:
Write a function `first_non_repeating_char(input_str)` that finds the first non-repeating character in a given string. The function should return the first character that appears only once in the string. If no such character exists, return `None`.
"""

def first_non_repeating_char(input_str): 
    """
    Finds the first non-repeating character in a given string.
    
    Args:
        input_str (str): The input string to search for the first non-repeating character.
    
    Returns:
        str or None: The first character that appears only once in the string, or None if no such character exists.
    """
    char_count = {}
 
    for ch in input_str: 
        if ch in char_count: 
            char_count[ch] += 1
        else: 
            char_count[ch] = 1
 
    for ch in input_str: 
        if char_count[ch] == 1: 
            return ch 
 
    return None