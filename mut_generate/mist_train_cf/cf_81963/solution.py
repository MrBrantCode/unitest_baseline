"""
QUESTION:
Write a function `Anagram(input)` that generates all unique alphanumeric sequences that can be formed using the characters of the input string without repeating the same digit or letter in a specific arrangement, considering the case of digits as important. The input string is an alphanumeric string.
"""

import itertools

def Anagram(input):
    return [''.join(p) for p in itertools.permutations(input)]