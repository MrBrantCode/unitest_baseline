"""
QUESTION:
Write a function called `find_valid_pairs` that takes a list of numbers and a target sum as input, and returns all pairs of numbers from the list that add up to the target sum. Each pair should contain distinct numbers and each number can only be used once.
"""

import itertools

def find_valid_pairs(numbers, target_sum):
    """
    This function takes a list of numbers and a target sum as input, 
    and returns all pairs of numbers from the list that add up to the target sum.
    
    Parameters:
    numbers (list): A list of numbers.
    target_sum (int): The target sum.
    
    Returns:
    list: A list of pairs of numbers that add up to the target sum.
    """
    # Use itertools to generate all possible combinations of length 2
    combinations = itertools.combinations(numbers, 2)
    # Filter the combinations to only include those that have the same sum
    valid_pairs = [pair for pair in combinations if sum(pair) == target_sum]
    return valid_pairs