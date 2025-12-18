"""
QUESTION:
Write a function `subsets_with_specific_elements(s, specific)` that takes a set `s` and a subset of elements `specific` as input, and returns all subsets of `s` that contain at least one element from `specific`. The function should return a list of tuples, where each tuple is a subset of `s` that meets the condition.
"""

import itertools

def subsets_with_specific_elements(s, specific):
    subsets = []
    n = len(s)
    
    # Generate all possible subsets
    for r in range(1, n+1):
        for subset in itertools.combinations(s, r):
            subsets.append(subset)
    
    # Filter subsets to include only those with at least one element from the specific subset
    subsets_with_specific = []
    for subset in subsets:
        if any(elem in specific for elem in subset):
            subsets_with_specific.append(subset)
    
    return subsets_with_specific