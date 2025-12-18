"""
QUESTION:
Write a function `is_anagram` that determines if two input strings are anagrams of each other. The function should return `True` if the strings are anagrams and `False` otherwise. The function should be case-sensitive and consider spaces and punctuation as part of the string.
"""

def is_anagram(s1, s2):
    """
    Determines if two input strings are anagrams of each other.
    
    Args:
    s1 (str): The first input string.
    s2 (str): The second input string.
    
    Returns:
    bool: True if the strings are anagrams, False otherwise.
    """
    return sorted(s1) == sorted(s2)