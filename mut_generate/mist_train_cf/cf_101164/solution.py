"""
QUESTION:
Write a function `get_permutations(s)` that generates all possible permutations of a given string `s` and returns them in a list of strings. The function should take a string `s` as input and return a list of strings, where each string is a permutation of `s`.
"""

from itertools import permutations
def entrance(s):
    perms = [''.join(p) for p in permutations(s)]
    return perms