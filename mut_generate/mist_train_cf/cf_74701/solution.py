"""
QUESTION:
Write a function named `unique_permutations` that takes a string `s` as input and returns a list of all unique permutations of the characters in `s`, sorted in alphabetical order. The function should be able to handle strings containing special characters and numbers.
"""

from itertools import permutations

def unique_permutations(s):
    # Generate all permutations
    perms = set(''.join(p) for p in permutations(s))

    # Convert the set to a list and sort it in alphabetical order
    return sorted(list(perms))