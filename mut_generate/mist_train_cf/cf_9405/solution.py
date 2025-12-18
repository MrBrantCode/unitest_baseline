"""
QUESTION:
Write a function `get_permutations(string)` that generates all unique permutations of the input string, considering that the string may contain duplicate characters.
"""

from itertools import permutations

def get_permutations(string):
    chars = list(string)
    perms = permutations(chars)
    result = [''.join(perm) for perm in perms]
    result = list(set(result))
    return result