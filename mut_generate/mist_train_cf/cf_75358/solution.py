"""
QUESTION:
Write a function `get_permutations(string)` that generates all possible permutations of the input string and returns them as a list of strings. The input string will only contain unique alphabetical characters.
"""

import itertools

def entrance(string):
    # Generate all permutations
    permutations = itertools.permutations(string)

    # Convert permutations to strings and add them to a list
    permutations_list = [''.join(permutation) for permutation in permutations]

    return permutations_list