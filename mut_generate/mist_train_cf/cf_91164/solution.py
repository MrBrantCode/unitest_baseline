"""
QUESTION:
Implement a function `is_anagram(str1, str2)` that checks if two input strings `str1` and `str2` are anagrams of each other. The function should ignore case sensitivity and non-alphabetic characters. It should return `True` if the strings are anagrams and `False` otherwise.
"""

import re

def is_anagram(str1, str2):
    # Step 1: Convert both strings to lowercase
    str1 = str1.lower()
    str2 = str2.lower()
    
    # Step 2: Remove all non-alphabetic characters
    str1 = re.sub(r'[^a-z]', '', str1)
    str2 = re.sub(r'[^a-z]', '', str2)
    
    # Step 3: Sort the characters of both strings and compare
    return sorted(str1) == sorted(str2)