"""
QUESTION:
Write a function `generate_permutations(seq)` that generates all possible permutations of characters in a given sequence `seq`. The sequence is a string of distinct alphabetic characters. The function should return a list of all permutations as strings.
"""

import itertools

def generate_permutations(seq):
    return [''.join(p) for p in itertools.permutations(seq)]