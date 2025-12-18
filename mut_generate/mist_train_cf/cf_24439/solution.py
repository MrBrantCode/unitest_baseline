"""
QUESTION:
Create a function `is_anagram` that determines if two input strings are anagrams of each other. The function should take two parameters: `string1` and `string2`, both of which are strings. The function should return `True` if `string1` and `string2` are anagrams, and `False` otherwise. The comparison should be case-insensitive.
"""

def is_anagram(string1, string2):
    """
    Determine if two input strings are anagrams of each other.
    
    Args:
    string1 (str): The first input string.
    string2 (str): The second input string.
    
    Returns:
    bool: True if string1 and string2 are anagrams, False otherwise.
    """
    return sorted(string1.lower()) == sorted(string2.lower())