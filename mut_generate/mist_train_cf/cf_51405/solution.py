"""
QUESTION:
Write a function `find_all_furthest_pairs` that takes a list of floats as input and returns a list of tuples containing two floats each, representing all possible pairs with maximum difference. The pairs should be ordered with the smaller value first, followed by the larger value. The function should return all such pairs, not just one. The input list is assumed to contain at least two elements.
"""

from typing import List, Tuple

def find_all_furthest_pairs(numbers: List[float]) -> List[Tuple[float, float]]:
    # find minimum and maximum values in the list
    min_val = min(numbers)
    max_val = max(numbers)
    
    # find all indices of min and max values
    min_idx = [idx for idx, val in enumerate(numbers) if val == min_val]
    max_idx = [idx for idx, val in enumerate(numbers) if val == max_val]
    
    # return all possible pairs of min and max values
    return [(min_val, max_val) for _ in range(len(min_idx) * len(max_idx))]