"""
QUESTION:
Create a function named `calc_geometric_mean` that takes an array of positive whole numbers as input and returns the geometric mean of the array. The function should not use the `statistics.geometric_mean` method. The input array can contain any number of positive whole numbers.
"""

from math import prod

def calc_geometric_mean(arr):
    """
    This function calculates the geometric mean of an array of positive whole numbers.

    Parameters:
    arr (list): A list of positive whole numbers.

    Returns:
    float: The geometric mean of the input array.
    """
    return prod(arr)**(1.0/len(arr))