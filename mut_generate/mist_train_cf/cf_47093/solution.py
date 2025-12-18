"""
QUESTION:
Write a function `get_permutations` that takes a list `arr` of unique integers and an integer `n` as input, and returns up to `n` unique permutations of `arr`. The function should return all permutations if `n` is greater than or equal to the total number of permutations. If `n` exceeds the total number of permutations, the function should indicate this and return all permutations.
"""

import itertools

def get_permutations(arr, n):
    # get unique permutations
    perms = list(itertools.permutations(arr))
    if n > len(perms):
        print("The number of requested permutations exceeds the total number of unique permutations for this list.")
    return perms[:n]