"""
QUESTION:
Write a function `generate_permutations(string)` that generates all possible permutations of a given string, where the string contains no duplicate characters. The function should return or print all permutations as strings.
"""

import itertools

def generate_permutations(string):
    # Get all permutations of the string
    permutations = itertools.permutations(string)

    # Return a list of permutations
    return [''.join(permutation) for permutation in permutations]