"""
QUESTION:
Create a function named `generate_subsets` that takes a set `my_set` and a positive integer `k` as input. The function should return all subsets of `my_set` with a maximum length of `k` elements. The input `k` should be validated to ensure it is within the range 1 <= k <= size of `my_set`. If `k` is outside this range, the function should return an error message.
"""

from itertools import combinations 

def generate_subsets(my_set, k):
    # Validate input  
    if k > len(my_set) or k < 1:
        return "Invalid input - 'k' should be in the range 1 <= k <= size of the set."

    # Create all possible subsets
    subsets = []
    for i in range(k+1):
        subsets.extend(combinations(my_set, i))

    return [list(subset) for subset in subsets]