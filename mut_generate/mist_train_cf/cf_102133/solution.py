"""
QUESTION:
Write a function named add_array_elements that calculates the sum of all elements in the input array and all possible combinations of three elements from the array. The function should take an array as input and return the sum of all elements and combinations. The function should also use memoization to optimize the calculation of the sum of combinations. The function should have a time complexity of O(m) where m is the length of the input array.
"""

from functools import lru_cache
from itertools import combinations

def add_array_elements(arr):
    """
    Calculate the sum of all elements in the input array and all possible combinations of three elements from the array.
    
    Args:
    arr (list): A list of integers.
    
    Returns:
    int: The sum of all elements and combinations.
    """
    
    # Calculate the sum of all elements in the array
    total_sum = sum(arr)
    
    # Use memoization to optimize the calculation of the sum of combinations
    @lru_cache(maxsize=None)
    def combination_sum(combination):
        return sum(combination)
    
    # Generate all possible combinations of three elements from the array
    combos = list(combinations(arr, 3))
    
    # Calculate the sum of all combinations
    combo_sum = sum(combination_sum(combo) for combo in combos)
    
    # Return the sum of all elements and combinations
    return total_sum + combo_sum