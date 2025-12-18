"""
QUESTION:
Create a function named `is_anagram` that takes two strings `str1` and `str2` as input. The function should ignore spaces, punctuation marks, and case when comparing the strings, and return `True` if `str1` and `str2` are anagrams of each other, and `False` otherwise.
"""

def is_anagram(str1, str2):
    # Remove spaces and punctuation marks from both strings
    str1 = ''.join(c.lower() for c in str1 if c.isalnum())
    str2 = ''.join(c.lower() for c in str2 if c.isalnum())
    
    # Check if the sorted strings are equal
    return sorted(str1) == sorted(str2)