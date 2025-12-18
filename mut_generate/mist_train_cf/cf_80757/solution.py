"""
QUESTION:
Generate a function `get_combinations(arr)` that prints and returns all combinations of unique integer elements from an array `arr` in ascending order. The function should allow repetition of numbers and be able to handle arrays of up to 1000 elements. The array `arr` contains unique integer elements and may be unsorted.
"""

import itertools

def get_combinations(arr):
    array_len = len(arr)
    arr.sort() 
    comb = []
    for r in range(1, array_len+1): 
        comb += list(itertools.combinations_with_replacement(arr, r))
    return comb