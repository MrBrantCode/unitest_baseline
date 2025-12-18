"""
QUESTION:
Create a function `generate_combinations` that takes a list as input and returns all unique combinations of exactly three elements from the list, where the order of the elements does not matter. The function should return a list of tuples, where each tuple represents a unique combination.
"""

import itertools

def generate_combinations(lst):
    combinations = list(itertools.combinations(lst, 3))
    return combinations