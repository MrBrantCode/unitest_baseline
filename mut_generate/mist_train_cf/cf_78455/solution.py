"""
QUESTION:
Design a function named `string_permutations(s)` that takes a string `s` as input and returns a list of all unique permutations of the string. The function should eliminate any duplicate permutations.
"""

import itertools

def string_permutations(s):
    # Get all permutations
    perms = list(itertools.permutations(s))
    # Convert permutations to strings
    str_perms = [''.join(p) for p in perms]
    # Use a set to eliminate duplicates
    unique_perms = set(str_perms)
    return list(unique_perms)