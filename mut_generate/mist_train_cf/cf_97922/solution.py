"""
QUESTION:
Write a function `generate_permutations` that takes a list of strings as input and returns all possible permutations of the strings. The function should return the permutations as a list of strings, where each permutation is a single string containing the characters of the input list in a different order.
"""

from itertools import permutations

def generate_permutations(strings):
    return [''.join(p) for p in permutations(strings)]