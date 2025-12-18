"""
QUESTION:
Create a function called `unique_permutations` that generates all unique permutations of a given string, considering case sensitivity and allowing special characters and numbers. The function should return a set of strings, each representing a unique permutation of the input string.
"""

import itertools

def unique_permutations(s):
    return set(''.join(p) for p in itertools.permutations(s))