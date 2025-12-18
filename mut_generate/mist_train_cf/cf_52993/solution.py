"""
QUESTION:
Write a function `find_permutations(s)` that takes a string `s` of distinct alphabetic characters as input and returns a list of all possible permutations of the characters in `s` in lexicographic sort order.
"""

import itertools

def find_permutations(s):
    return [''.join(p) for p in itertools.permutations(s)]