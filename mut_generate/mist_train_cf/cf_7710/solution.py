"""
QUESTION:
Write a function called `is_prime` that takes an integer `num` as input and returns a boolean value indicating whether `num` is prime or not. The function should iterate from 2 up to the square root of `num`, checking for divisibility, and return `False` if `num` is divisible by any number in this range. If no divisor is found, the function should return `True`.
"""

import math

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True