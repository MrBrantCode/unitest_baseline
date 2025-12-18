"""
QUESTION:
Write a function named `check_permutations` that takes two strings as input and returns a boolean indicating whether one string is a permutation of the other. The function should be case-sensitive and consider spaces and punctuation as characters. It should return `True` if one string is a permutation of the other, and `False` otherwise.
"""

def check_permutations(str1, str2):
    return sorted(str1) == sorted(str2)