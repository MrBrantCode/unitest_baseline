"""
QUESTION:
Write a function `is_anagram(s1, s2)` that checks if two given strings `s1` and `s2` are anagrams, ignoring any punctuation and white spaces. The function should have a time complexity of O(nlogn) and a space complexity of O(1). The function should return `True` if the strings are anagrams and `False` otherwise.
"""

import re

def is_anagram(s1, s2):
    """
    Checks if two given strings are anagrams, ignoring any punctuation and white spaces.

    Args:
        s1 (str): The first string.
        s2 (str): The second string.

    Returns:
        bool: True if the strings are anagrams, False otherwise.
    """
    # Remove white spaces and punctuation from both strings
    s1 = re.sub('[\W_]+', '', s1.lower())
    s2 = re.sub('[\W_]+', '', s2.lower())

    # If the lengths of s1 and s2 are not equal, return False
    if len(s1) != len(s2):
        return False

    # Sort s1 and s2 in ascending order
    s1 = sorted(s1)
    s2 = sorted(s2)

    # Compare each character in the sorted s1 with the corresponding character in the sorted s2
    return s1 == s2