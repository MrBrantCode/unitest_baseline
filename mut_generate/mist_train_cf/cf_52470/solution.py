"""
QUESTION:
Write a function `permutations_of_string(s)` that generates all unique permutations of the input string `s` without repeating any character in each permutation. The input string only contains unique characters.
"""

import itertools

def permutations_of_string(s):
    return [''.join(p) for p in itertools.permutations(s)]