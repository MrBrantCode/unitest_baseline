"""
QUESTION:
Design a function `all_permutations(lst)` that takes a list of characters as input and returns a list of all possible permutations of these characters as strings. Each permutation should be a unique arrangement of all characters in the input list.
"""

import itertools

def all_permutations(lst):
    # getting all permutations
    perms = itertools.permutations(lst)
    
    # returning as a list of strings
    return [''.join(p) for p in perms]