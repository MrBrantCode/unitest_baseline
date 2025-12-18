"""
QUESTION:
Create a function `char_count` that takes a string as input and returns a tuple containing the total character count and a dictionary with the count of individual unique characters (ignoring case sensitivity). The function should handle special characters and white spaces.
"""

def char_count(s):
    """
    Returns a tuple containing the total character count and a dictionary 
    with the count of individual unique characters (ignoring case sensitivity).

    Args:
    s (str): The input string.

    Returns:
    tuple: A tuple containing total character count and a dictionary with unique character counts.
    """
    s = s.lower()
    total_count = len(s)
    unique_count = {}
    
    for char in s:
        if char in unique_count:
            unique_count[char] += 1
        else:
            unique_count[char] = 1
            
    return total_count, unique_count