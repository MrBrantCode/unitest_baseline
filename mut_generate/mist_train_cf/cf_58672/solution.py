"""
QUESTION:
Write a function `get_permutations` that takes a string of strictly upper-case alphabets as input and returns a list of all possible permutations of the input string. The input string will only contain alphabets.
"""

import itertools

def get_permutations(string):
    return [''.join(p) for p in itertools.permutations(string)]