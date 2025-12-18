"""
QUESTION:
Create a function `is_prime_number` that takes a positive integer `num` as input and returns a boolean value indicating whether the number is a prime number or not. The function should return `True` if `num` is a prime number and `False` otherwise, with a time complexity of O(sqrt(n)). Do not use any built-in functions or libraries to determine whether a number is a prime number.
"""

import math

def is_prime_number(num):
    if num < 2:
        return False
    for i in range(2, math.isqrt(num) + 1):
        if num % i == 0:
            return False
    return True