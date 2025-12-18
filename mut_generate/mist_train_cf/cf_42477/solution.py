"""
QUESTION:
Implement a function `count_group_invariant_inputs(inputs)` that takes a list of boolean values `inputs` and returns the count of group invariant inputs present in the list. A group invariant input is a subset of boolean values with cardinality greater than 1 that remains unchanged when permuted. The function should consider all possible subsets of the input list.
"""

from itertools import combinations, permutations

def count_group_invariant_inputs(inputs):
    # Generate all subsets of cardinality > 1
    subsets = [combo for r in range(2, len(inputs) + 1) for combo in combinations(inputs, r)]
    
    count = 0
    for subset in subsets:
        # Check if the subset remains unchanged when permuted
        unchanged = all(tuple(p) in subsets for p in permutations(subset))
        if unchanged:
            count += 1
    
    return count