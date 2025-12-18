"""
QUESTION:
Write a function `generate_combinations` that takes a list of integers as input and returns a list of all unique combinations of exactly three elements from the list, with the order of the elements in each combination in increasing order and without duplicates.
"""

from itertools import combinations

def generate_combinations(lst):
    # Remove duplicates and sort the list
    lst = sorted(list(set(lst)))
    
    # Generate all combinations of 3 elements
    combinations_list = list(combinations(lst, 3))
    
    # Remove combinations that are not in increasing order
    combinations_list = [combo for combo in combinations_list if combo == tuple(sorted(combo))]
    
    return combinations_list