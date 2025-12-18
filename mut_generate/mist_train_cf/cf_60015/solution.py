"""
QUESTION:
Write a function `compare_strings` that takes two strings `str1` and `str2` as input and returns the number of characters that are different in those strings. The function should be case-sensitive and account for Unicode characters. It should also be able to handle strings of different lengths.
"""

from itertools import zip_longest

def compare_strings(str1: str, str2: str) -> int:
    count = sum(1 for a, b in zip_longest(str1, str2) if a != b)
    return count