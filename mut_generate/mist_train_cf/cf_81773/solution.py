"""
QUESTION:
Create a function `combine_reverse_capitalize` that takes two strings as input, combines them, reverses the order of characters, and capitalizes the resulting string. The function should return a tuple containing the transformed string and its length.
"""

def combine_reverse_capitalize(s1, s2):
    """
    Combines two strings, reverses the order of characters, and capitalizes the resulting string.
    
    Args:
        s1 (str): The first string.
        s2 (str): The second string.
    
    Returns:
        tuple: A tuple containing the transformed string and its length.
    """
    combined = s1 + s2
    reversed_str = combined[::-1]
    capitalized = reversed_str.upper()
    length = len(capitalized)
    return capitalized, length