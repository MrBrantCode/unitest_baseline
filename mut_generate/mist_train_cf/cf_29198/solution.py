"""
QUESTION:
Write a function `calculate_combinations` that takes a list `nk` containing three positive integers and an optional parameter `verbose` (defaulting to 0) as input. The first two integers in the list represent the total number of items `n` and the number of items to choose `k`, respectively. The function should calculate the number of combinations of choosing `k` items from `n` items and return the result. If `verbose` is set to 1, the function should also print the number of combinations and the actual combinations. Assume that the input list `nk` will always contain exactly three positive integers.
"""

from itertools import combinations

def calculate_combinations(nk, verbose=0):
    n, k, _ = nk
    comb = list(combinations(range(1, n+1), k))
    num_combinations = len(comb)
    if verbose:
        print(f"Number of combinations for choosing {k} items from {n} items: {num_combinations}")
        print("Combinations:")
        for c in comb:
            print(c)
    return num_combinations