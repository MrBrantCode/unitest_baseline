"""
QUESTION:
Create a function called `generate_combinations` that takes a list of integers as input and returns all unique combinations of exactly three elements, where the elements in each combination are in increasing order and the order of the elements does not matter. The input list may contain duplicate elements.
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