"""
QUESTION:
Implement a function called `is_anagram` that checks if two input strings are anagrams. The function should take two strings as input and return `True` if the strings are anagrams, and `False` otherwise. The comparison should be case-insensitive and ignore non-alphabetic characters.
"""

import re

def is_anagram(str1, str2):
    # Convert both strings to lowercase
    str1 = str1.lower()
    str2 = str2.lower()

    # Remove non-alphabetic characters
    str1 = re.sub('[^a-z]', '', str1)
    str2 = re.sub('[^a-z]', '', str2)

    # Sort the characters and compare
    return sorted(str1) == sorted(str2)