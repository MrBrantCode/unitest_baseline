"""
QUESTION:
Write a function `find_valid_pairs` that takes a list of integers and a target sum as input. The function should return all unique pairs of numbers in the list that add up to the target sum, without using any number more than once. The pairs should be returned as a list of tuples.
"""

import itertools

def find_valid_pairs(numbers, target_sum):
    """
    This function takes a list of integers and a target sum as input.
    It returns all unique pairs of numbers in the list that add up to the target sum, 
    without using any number more than once.
    
    Args:
        numbers (list): A list of integers.
        target_sum (int): The target sum.
    
    Returns:
        list: A list of tuples, where each tuple is a pair of numbers that add up to the target sum.
    """
    # Use itertools to generate all possible combinations of length 2
    combinations = itertools.combinations(numbers, 2)
    # Filter the combinations to only include those that have the same sum
    valid_pairs = [pair for pair in combinations if sum(pair) == target_sum]
    return valid_pairs