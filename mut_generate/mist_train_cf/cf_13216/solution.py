"""
QUESTION:
Write a function `is_anagram(s1, s2)` that checks if two input strings `s1` and `s2` are anagrams, considering all characters including spaces and punctuation marks, and taking their case into account. Return `True` if `s1` and `s2` are anagrams, otherwise return `False`.
"""

def entance(s1, s2):
    # Remove spaces and punctuation marks and convert to lowercase
    s1 = ''.join(c.lower() for c in s1 if c.isalnum())
    s2 = ''.join(c.lower() for c in s2 if c.isalnum())

    # Check if the sorted strings are equal
    return sorted(s1) == sorted(s2)