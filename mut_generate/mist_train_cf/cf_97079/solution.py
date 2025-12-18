"""
QUESTION:
Write a function called `generate_permutations(s)` to generate all unique permutations of a given input string `s` that may contain duplicate characters. The function should return a list of unique permutations as strings and have a time complexity of O(n!), where n is the length of the input string `s`.
"""

from itertools import permutations

def generate_permutations(s):
    # Use set to remove duplicates
    return list(set([''.join(p) for p in permutations(s)]))