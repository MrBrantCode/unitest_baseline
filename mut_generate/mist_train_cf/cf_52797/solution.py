"""
QUESTION:
Design a function named `all_permutations` that generates and returns every possible permutation of a given input string. The function should take one parameter: the input string. The permutations should be generated in lexicographic sort order.
"""

from itertools import permutations

def all_permutations(s):
    perms = permutations(s)
    perm_list = ["".join(p) for p in perms]
    return perm_list