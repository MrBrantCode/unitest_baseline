"""
QUESTION:
Write a function `is_prime(num)` that takes an integer as input and returns a boolean value indicating whether the number is prime or not. The function should return `False` for numbers less than or equal to 1 and `True` if the number is divisible by no natural numbers other than 1 and itself, and `False` otherwise.
"""

import math

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, math.isqrt(num) + 1):
        if num % i == 0:
            return False
    return True