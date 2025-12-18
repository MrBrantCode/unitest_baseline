"""
QUESTION:
Write a Python function named `generate_permutations` that takes a list of unique alphabetic characters as input and returns a list of all possible permutations of these characters as strings.
"""

from itertools import permutations

def generate_permutations(data):
    perms = permutations(data)
    return [''.join(p) for p in perms]