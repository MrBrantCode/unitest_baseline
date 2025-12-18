"""
QUESTION:
Create a function `check_anagram` that takes two strings as input and returns whether they are anagrams of each other. The function should ignore case sensitivity, whitespace characters, and non-alphabetic characters. The function should have a time complexity of O(n log n) or better, where n is the length of the shorter string.
"""

import re

def check_anagram(string1, string2):
    """
    Checks if two strings are anagrams of each other, ignoring case sensitivity, 
    whitespace characters, and non-alphabetic characters.

    Args:
        string1 (str): The first string.
        string2 (str): The second string.

    Returns:
        bool: True if the strings are anagrams, False otherwise.
    """
    # Remove whitespace characters and non-alphabetic characters, and convert to lowercase
    string1 = re.sub('[\W_]+', '', string1).lower()
    string2 = re.sub('[\W_]+', '', string2).lower()

    # Compare the sorted lists of characters
    return sorted(string1) == sorted(string2)