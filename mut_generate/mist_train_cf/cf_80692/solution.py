"""
QUESTION:
Write a function named `find_subsets(s, n)` that takes a string `s` and a specific string length `n` as inputs and returns a set of all unique permutations of letters from `s` with the specified length. The order of characters in each permutation does not matter, and the function should consider cases where the target string contains duplicate letters. The function should exclude duplicate permutations from the result.
"""

from itertools import permutations

def find_subsets(s, n):
    distinct_s = "".join(set(s))
    subsets = permutations(distinct_s, n)
    return set(subsets)