"""
QUESTION:
Create a function `is_triangular(n)` that takes an integer `n` as input and returns a tuple where the first element is a boolean indicating whether `n` is a triangular number and the second element is the position of `n` in the triangular series if it exists, otherwise `None`. The function should be able to handle large numbers efficiently, ideally in constant time and space.
"""

import math

def is_triangular(n):
    """
    Checks if a number 'n' is triangular and returns its position in the series.
    
    Args:
    n (int): The number to check.
    
    Returns:
    tuple: A tuple containing a boolean indicating whether 'n' is triangular and its position in the series if it exists, otherwise None.
    """
    i = (math.sqrt(8*n + 1) - 1) / 2
    return i.is_integer(), int(i) if i.is_integer() else None