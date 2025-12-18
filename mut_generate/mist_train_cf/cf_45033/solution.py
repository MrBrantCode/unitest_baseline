"""
QUESTION:
Create a function named `get_combinations` that takes a set as input and returns a list of all unique combinations of various lengths from the set without repetition, including the empty set. The function should work with sets containing numbers, strings, and mixed data types.
"""

from itertools import chain, combinations

def get_combinations(my_set):
    return list(chain(*[combinations(my_set, i) for i in range(len(my_set) + 1)]))