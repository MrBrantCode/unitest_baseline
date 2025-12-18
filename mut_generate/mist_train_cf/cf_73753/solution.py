"""
QUESTION:
Write a function `isTriangular(num)` that determines whether a given integer `num` is a triangular number or not. A triangular number is a figurate number that represents a triangle. The function should return `True` if the number is triangular and `False` otherwise. The input will be an integer, and the function should not take any other parameters.
"""

import math

def isTriangular(num):
    """
    Determines whether a given integer is a triangular number or not.
    
    A triangular number is a figurate number that represents a triangle.
    
    Args:
    num (int): The number to check.
    
    Returns:
    bool: True if the number is triangular, False otherwise.
    """
    n = 8 * num + 1
    sqrt = int(math.sqrt(n))
    return pow(sqrt, 2) == n