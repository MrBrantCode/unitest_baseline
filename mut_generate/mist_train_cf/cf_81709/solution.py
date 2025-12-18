"""
QUESTION:
Create a function `get_combinations` that takes an array of integers and returns all possible combinations of three numbers from the array. The function should use the itertools library.
"""

import itertools

def get_combinations(arr):
    """
    Returns all possible combinations of three numbers from the given array.
    
    Parameters:
    arr (list): The input array of integers.
    
    Returns:
    list: A list of tuples, where each tuple is a combination of three numbers from the array.
    """
    return list(itertools.combinations(arr, 3))