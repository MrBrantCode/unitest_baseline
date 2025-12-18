"""
QUESTION:
Write a function `get_permutations(s)` that takes a string `s` as input and returns a list of all unique permutations of the string. The function should handle cases where the input string contains repeated characters.
"""

import itertools

def get_permutations(s):
    # Generate all permutations of the string
    perms = itertools.permutations(s)
    
    # Convert the permutations to a list and remove duplicates
    unique_perms = list(set(perms))
    
    # Convert the permutations back to strings and return the list
    return [''.join(perm) for perm in unique_perms]