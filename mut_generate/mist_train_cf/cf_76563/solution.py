"""
QUESTION:
Write a function `find_highest_sum_quartet` that takes a list of integers as input and returns the quartet of numbers that yields the highest possible sum. The function should consider all possible combinations of four numbers in the input list.
"""

import itertools

def find_highest_sum_quartet(arr):
    """
    This function takes a list of integers as input and returns the quartet of numbers that yields the highest possible sum.
    
    Parameters:
    arr (list): A list of integers.
    
    Returns:
    tuple: The quartet of numbers with the highest possible sum.
    """
    combs = list(itertools.combinations(arr, 4))  # generate all possible combinations of four numbers from the array
    return max(combs, key=sum)  # choose the quartet with the highest sum