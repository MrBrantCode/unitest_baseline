"""
QUESTION:
Write a function `find_valid_pairs` that takes a list of distinct integers as input and returns all pairs of numbers with the same sum. Each pair should contain two different numbers and each number can only be used once. The function should use the `itertools` module in Python.
"""

import itertools

def find_valid_pairs(numbers):
    """
    Finds all pairs of numbers with the same sum in a given list of distinct integers.
    
    Args:
    numbers (list): A list of distinct integers.
    
    Returns:
    list: A list of pairs of numbers with the same sum.
    """
    target_sum = sum(numbers) // 2
    combinations = itertools.combinations(numbers, 2)
    valid_pairs = [pair for pair in combinations if sum(pair) == target_sum]
    return valid_pairs