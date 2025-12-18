"""
QUESTION:
Write a function named `generate_permutations` that takes an input string and returns all unique permutations of the string as a list. The function should handle duplicate characters in the input string.
"""

from itertools import permutations

def generate_permutations(string):
    chars = list(string)
    perms = permutations(chars)
    result = [''.join(perm) for perm in perms]
    result = list(set(result))
    return result