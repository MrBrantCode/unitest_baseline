"""
QUESTION:
Write a function `is_cube_of_prime(b)` that takes an integer `b` as input, where 0 ≤ `b` ≤ 2000, and returns `True` if `b` is the cube of a prime number, and `False` otherwise.
"""

import math

def is_cube_of_prime(b):
    # Check if the number is a perfect cube
    cube_root = round(b ** (1. / 3.))
    if cube_root**3 != b:
        return False

    # Check if cube root is a prime number
    for i in range(2, int(math.sqrt(cube_root))+1):
        if cube_root % i == 0:  
            return False  # cube root is not a prime number
    return True