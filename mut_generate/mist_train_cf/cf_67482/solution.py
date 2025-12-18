"""
QUESTION:
Create a function called `get_permutations` that takes a string `s` as input and returns a list of all possible permutations of the characters in the string. The function should return the permutations as a list of strings.
"""

import itertools

def get_permutations(s):
    return [''.join(p) for p in itertools.permutations(s)]