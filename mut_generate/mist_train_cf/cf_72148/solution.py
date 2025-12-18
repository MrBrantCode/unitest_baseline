"""
QUESTION:
Generate a function named `generate_rearrangements` that takes two parameters: a list of numerical elements `arr` and an integer `n`. The function should return the first `n` distinct rearrangements of the elements in `arr`. If `n` is greater than the total number of possible rearrangements, return an error message stating the maximum possible rearrangements.
"""

import itertools

def generate_rearrangements(arr, n):
    permutations = list(itertools.permutations(arr))
    
    if n > len(permutations):
        return f"Cannot generate {n} permutations, the maximum for this list is {len(permutations)}"
    
    return permutations[:n]