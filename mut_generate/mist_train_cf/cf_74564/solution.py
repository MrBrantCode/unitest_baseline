"""
QUESTION:
Write a Python function `unique_combinations` that generates all unique combinations of elements in a given list, disregarding duplicate combinations and the order of elements within a combination. The function should return a list of tuples, where each tuple is a unique combination of elements from the input list. The input list can contain duplicate elements.
"""

from itertools import combinations

def unique_combinations(lst):
    # Use set to avoid duplicates
    unique_combinations = set()
    
    # Generate all combinations and add unique combinations to set
    for r in range(len(lst) + 1):
        for subset in combinations(lst, r):
            unique_combinations.add(subset)
    
    # Convert back to list
    return list(unique_combinations)