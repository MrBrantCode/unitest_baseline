"""
QUESTION:
Write a function `check_permutation(str1, str2)` that checks whether two input strings are permutations of each other. The function should return `True` if the strings are permutations, and `False` otherwise.
"""

from collections import Counter

def check_permutation(str1, str2):
    """Checks whether two input strings are permutations of each other."""
    return Counter(str1) == Counter(str2)