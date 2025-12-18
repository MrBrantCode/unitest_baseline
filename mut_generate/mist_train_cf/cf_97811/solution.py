"""
QUESTION:
Write a function `find_valid_pairs` that takes a list of integers and a target sum as input, and returns all pairs of distinct numbers from the list that add up to the target sum. Each number can only be used once, and the pairs cannot contain the same number twice.
"""

import itertools

def find_valid_pairs(numbers, target_sum):
    """
    This function finds all pairs of distinct numbers from the list that add up to the target sum.
    
    Args:
    numbers (list): A list of integers.
    target_sum (int): The target sum that the pairs should add up to.
    
    Returns:
    list: A list of pairs of distinct numbers that add up to the target sum.
    """
    # Use itertools to generate all possible combinations of length 2
    combinations = itertools.combinations(numbers, 2)
    # Filter the combinations to only include those that have the same sum
    valid_pairs = [pair for pair in combinations if sum(pair) == target_sum]
    return valid_pairs