"""
QUESTION:
Implement a function named `possible_combinations` that takes a list as an input and returns all possible combinations of length 3 from the given list. The order of elements should not be considered, i.e., (1, 2, 3) and (3, 2, 1) are considered the same combination.
"""

from itertools import combinations

def possible_combinations(lst):
    return list(combinations(lst, 3))