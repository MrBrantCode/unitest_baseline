"""
QUESTION:
Write a function named `generate_permutations` that takes a string of consecutive characters as input and returns all possible permutations of the characters in the string. The function should return the permutations as a list of strings.
"""

import itertools

def generate_permutations(sequence):
    return [''.join(p) for p in itertools.permutations(sequence)]