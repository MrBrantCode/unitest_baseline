"""
QUESTION:
Write a function `is_permutation(string1, string2)` that determines if one string is a permutation of the other. The function should take two strings as input and return a boolean value. The function should be case-sensitive and should consider spaces and punctuation as characters. The strings may contain duplicate characters.
"""

def is_permutation(string1, string2):
    if len(string1) != len(string2):
        return False
    return sorted(string1) == sorted(string2)