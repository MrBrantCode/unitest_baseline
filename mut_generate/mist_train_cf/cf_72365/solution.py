"""
QUESTION:
Write a function called `string_permutations(s)` that takes an ASCII input string `s` as its argument and returns all distinct permutations of the supplied characters, preserving the occurrence and positioning of each character in the given string. The function should return a list of strings, each representing a permutation of the input string.
"""

import itertools

def string_permutations(s):
    return [''.join(p) for p in set(itertools.permutations(s))]