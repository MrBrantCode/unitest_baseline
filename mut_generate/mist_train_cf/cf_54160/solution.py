"""
QUESTION:
Create a function named `lowest_common_multiple` that takes two integer arguments `x` and `y`. Implement the function to return the Least Common Multiple (LCM) of `x` and `y`. The function should be able to handle both positive and negative integers.
"""

import math

def lowest_common_multiple(x, y):
    return abs(x*y) // math.gcd(x, y)