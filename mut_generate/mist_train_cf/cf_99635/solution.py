"""
QUESTION:
Write a function `get_permutations(s)` that generates all possible permutations of the input string `s` and returns them as a list of strings.
"""

from itertools import permutations
def get_permutations(s):
    perms = [''.join(p) for p in permutations(s)]
    return perms