"""
QUESTION:
Develop a function named `find_combinations` that takes two parameters: a target numerical value and an array of integers. The function should return all combinations of index positions in the array where the corresponding elements sum up to the target value.
"""

import itertools

def find_combinations(target, arr):
    all_combinations = []
    # Get all index combinations
    for r in range(1, len(arr) + 1):
        combinations_object = itertools.combinations(range(len(arr)), r)
        combinations = [combo for combo in combinations_object]
        all_combinations.extend(combinations)
    # Get combinations whose elements sum to the target
    valid_combinations = [combo for combo in all_combinations if sum(arr[i] for i in combo) == target]
    return valid_combinations