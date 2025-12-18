"""
QUESTION:
Create a function `check_prime(n)` that takes an integer `n` as input and returns "True" if it's a prime number and "False" otherwise. The function should optimize its execution time by checking for divisibility up to the square root of `n` instead of all the way to `n` itself and skip even numbers (except 2) in its check. The solution should balance space and time complexity. The input `n` is an integer and the output is a boolean value.
"""

import math

def check_prime(n):
    """Returns true for prime numbers and false for non-prime numbers; improves performance using a rarely-employed optimization technique. 
    """
    if n < 2:
        return False
    if n == 2: 
        return True
    if n % 2 == 0:
        return False
    max_factor = math.isqrt(n)
    for factor in range(3, max_factor + 1, 2):
        if n % factor == 0:
            return False
    return True