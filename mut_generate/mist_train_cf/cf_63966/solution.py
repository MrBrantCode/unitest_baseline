"""
QUESTION:
Write a function called `character_counts` that takes a string as input and returns a dictionary where each key is a unique character in the string and each value is the count of that character. The function should not include any duplicate characters in the dictionary keys.
"""

from collections import Counter

def character_counts(s):
    """
    Returns a dictionary where each key is a unique character in the string 
    and each value is the count of that character.
    
    Args:
        s (str): The input string.
    
    Returns:
        dict: A dictionary with character counts.
    """
    return dict(Counter(s))