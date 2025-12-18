"""
QUESTION:
Compute the function `compute_pi(n)` that calculates Pi to the nth decimal place. The function should take an integer `n` as input and return the value of Pi rounded to the nth decimal place.
"""

import math

def compute_pi(n):
    """
    Calculate Pi to the nth decimal place.

    Args:
    n (int): The number of decimal places to round Pi to.

    Returns:
    float: The value of Pi rounded to the nth decimal place.
    """
    return round(math.pi, n)