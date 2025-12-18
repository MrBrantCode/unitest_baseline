"""
QUESTION:
Create a function `is_prime` that takes a single integer `num` as input and returns `True` if `num` is prime, `False` if `num` is composite, and `None` if `num` is non-numeric, negative, 0, or 1. The function must have a time complexity less than O(n log(n)).
"""

import math

def is_prime(num):
    """
    Checks if a number is prime, composite, or non-numeric.
    
    Args:
    num: The number to check.
    
    Returns:
    True if num is prime, False if num is composite, and None if num is non-numeric, negative, 0, or 1.
    """
    return all([(num%j) for j in range(2, int(math.sqrt(num))+1)]) if isinstance(num, int) and num > 1 else None