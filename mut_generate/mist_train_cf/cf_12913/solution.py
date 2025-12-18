"""
QUESTION:
Write a function called `combination` that calculates the number of ways to choose k items from a list of n options. The function should take two parameters, n and k, where k is less than or equal to n, and return the number of combinations as an integer.
"""

import math

def combination(n, k):
    """
    Calculate the number of ways to choose k items from a list of n options.

    Args:
        n (int): The total number of options.
        k (int): The number of items to choose.

    Returns:
        int: The number of combinations.
    """
    return math.comb(n, k)