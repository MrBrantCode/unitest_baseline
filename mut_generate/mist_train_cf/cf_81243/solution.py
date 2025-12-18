"""
QUESTION:
Create a Python function named `unique_permutations` that takes a list as an argument and returns every unique permutation of the elements within the given list. The list elements can be of any data type (including lists, strings, or dictionaries) and the function should handle these data types while avoiding repetitions of permutations.
"""

import itertools

def unique_permutations(lst):
    """
    Function to compute every unique permutation of elements within a given list
    """
    return list(itertools.permutations(lst))