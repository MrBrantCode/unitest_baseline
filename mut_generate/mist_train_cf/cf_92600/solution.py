"""
QUESTION:
Write a function `generate_combinations` that takes a list `lst` as input and returns all combinations of exactly three elements from the list, where the order of the elements does not matter.
"""

import itertools

def generate_combinations(lst):
    combinations = list(itertools.combinations(lst, 3))
    return combinations