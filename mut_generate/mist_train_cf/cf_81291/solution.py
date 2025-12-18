"""
QUESTION:
Write a function `check_if_permutation(str1, str2)` that determines whether two input strings `str1` and `str2` are permutations of one another, considering only the alphabetical symbols and their quantities, regardless of order. The function should return `True` if the strings are permutations and `False` otherwise.
"""

from collections import Counter

def check_if_permutation(str1, str2):
    # Remove non-alphabetical characters and convert to lower case
    str1 = ''.join(filter(str.isalpha, str1)).lower()
    str2 = ''.join(filter(str.isalpha, str2)).lower()
    
    return Counter(str1) == Counter(str2)