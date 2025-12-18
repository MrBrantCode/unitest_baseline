"""
QUESTION:
Write a function named `compute_permutations` that takes an input string and returns a list of all possible permutations of the input string, with each permutation represented as a string. The input string will only contain unique characters.
"""

import itertools

def compute_permutations(input_string):
    return [''.join(p) for p in itertools.permutations(input_string)]