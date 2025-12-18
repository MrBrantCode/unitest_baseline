"""
QUESTION:
Create a function called `unique_permutations` that accepts a list of integers as input and returns a 2D list of every unique permutation of that list, respecting the original order of duplicate entries. The function should handle duplicate entries, return unique permutations only once, and maintain the relative position of identical elements from the input list in the output permutations.
"""

from itertools import permutations

def unique_permutations(lst):
    perm_set = set(permutations(lst, len(lst)))
    unique_perms = []
    for perm in perm_set:
        indexes = [perm.index(x) for x in perm if lst.count(x) > 1]
        if indexes == sorted(indexes):
            unique_perms.append(list(perm))
    return unique_perms