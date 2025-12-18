"""
QUESTION:
Write a function called `compute_square_root` that takes a positive integer `N` as input, calculates its square root, stores the result in the variable `output`, rounds the `output` to the nearest integer, and stores the rounded result in the variable `rounded_output`. The function should handle cases where the square root is not an integer.
"""

import math

def compute_square_root(N):
    """
    This function calculates the square root of a positive integer N, 
    rounds the result to the nearest integer, and returns both values.

    Args:
        N (int): A positive integer.

    Returns:
        tuple: A tuple containing the square root of N and its rounded value.
    """
    output = math.sqrt(N)
    rounded_output = round(output)
    return output, rounded_output