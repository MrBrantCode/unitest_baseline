"""
QUESTION:
Write a function named `find_permutations` that takes a list of distinct elements as input and returns all its unique permutations. The function should return the permutations as a list of tuples, where each tuple represents a permutation.
"""

from itertools import permutations

def find_permutations(lst):
    """Return all unique permutations of a list of distinct elements."""
    return list(permutations(lst))