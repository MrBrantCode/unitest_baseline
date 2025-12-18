"""
QUESTION:
Write a function `subsets_with_specific_elements(s, specific)` that takes two sets `s` and `specific` as input, and returns all subsets of `s` that contain at least one element from `specific`.
"""

import itertools

def subsets_with_specific_elements(s, specific):
    subsets = []
    n = len(s)
    
    for r in range(1, n+1):
        for subset in itertools.combinations(s, r):
            subsets.append(subset)
    
    subsets_with_specific = [subset for subset in subsets if any(elem in specific for elem in subset)]
    
    return subsets_with_specific