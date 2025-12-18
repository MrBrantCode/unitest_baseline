"""
QUESTION:
Design a function `is_anagram` that takes two string type variables as arguments and determines if the two strings are anagrams of each other. The function should return `True` if the strings are anagrams and `False` otherwise. Assume the input strings are already in lower case and do not contain any punctuation or special characters.
"""

def is_anagram(s1, s2):
    """
    Checks if two strings are anagrams of each other.

    Args:
        s1 (str): The first string.
        s2 (str): The second string.

    Returns:
        bool: True if the strings are anagrams, False otherwise.

    """
    # If the lengths of the strings are not equal, they cannot be anagrams.
    if len(s1) != len(s2):
        return False
    
    # Sort the letters in the strings and compare them.
    return sorted(s1) == sorted(s2)