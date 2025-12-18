"""
QUESTION:
Implement a function named `is_anagram` that checks if two input strings are anagrams, returning `True` if they are and `False` otherwise. The function should ignore case differences and non-alphabetic characters, and it should handle strings of different lengths and empty strings correctly.
"""

import re

def is_anagram(str1, str2):
    # Convert both strings to lowercase
    str1 = str1.lower()
    str2 = str2.lower()

    # Remove non-alphabetic characters
    str1 = re.sub('[^a-z]', '', str1)
    str2 = re.sub('[^a-z]', '', str2)

    # Sort the characters and compare the sorted strings
    return sorted(str1) == sorted(str2)