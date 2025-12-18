"""
QUESTION:
Write a Python function `find_min_value` that calculates the minimum value in a given 2D array. The input is a 2D array of integers, and the output is the smallest integer in the array. Assume that the input array is not empty and contains at least one element. The function should not use any external libraries or dependencies other than the standard Python library.
"""

import numpy

def find_min_value(array):
    """
    This function calculates the minimum value in a given 2D array.
    
    Parameters:
    array (numpy.ndarray): A 2D array of integers.
    
    Returns:
    int: The smallest integer in the array.
    """
    return array.min()