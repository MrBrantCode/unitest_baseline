"""
QUESTION:
Write a function `is_anagram(str1, str2)` that takes two strings as input and returns a boolean indicating whether they are anagrams of each other, ignoring spaces and punctuation marks, and considering all characters in lowercase.
"""

def entance(str1, str2):
    # Remove spaces and punctuation marks from both strings
    str1 = ''.join(c.lower() for c in str1 if c.isalnum())
    str2 = ''.join(c.lower() for c in str2 if c.isalnum())
    
    # Check if the sorted strings are equal
    return sorted(str1) == sorted(str2)