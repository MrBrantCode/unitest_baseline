"""
QUESTION:
Generate a function named `generate_permutations` that returns all possible permutations of N distinct numeric entities. The function should take an integer `N` as input and return a list of tuples, where each tuple is a unique permutation of numbers from 1 to `N`.
"""

import itertools

def generate_permutations(N):
    numbers = list(range(1, N + 1))
    permutations = list(itertools.permutations(numbers))
    return permutations