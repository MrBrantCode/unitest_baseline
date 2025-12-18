"""
QUESTION:
Write a function `generate_perms` that takes a list of items as input and returns a list of unique permutations in lexicographic order. Additionally, write a function `get_neighbours` that takes a sorted list of permutations and a target permutation as input, and returns the lexicographically previous and next permutation of the target. Assume that the input list contains unique elements.
"""

import itertools

def generate_perms(elements):
    return sorted(list(set(itertools.permutations(elements))))

def get_neighbours(perms, target):
    index = perms.index(target)
    prev_perm = perms[index - 1] if index != 0 else None
    next_perm = perms[index + 1] if index != len(perms) - 1 else None
    return prev_perm, next_perm