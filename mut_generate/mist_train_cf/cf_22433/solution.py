"""
QUESTION:
Write a function `generate_permutations(s)` that generates all unique permutations of a given string `s` with duplicate characters. The function should return a list of strings, each representing a unique permutation of the input string. The time complexity of the function should be O(n!), where n is the length of the input string.
"""

from itertools import permutations

def generate_permutations(s):
    # Use set to remove duplicates
    return list(set([''.join(p) for p in permutations(s)]))