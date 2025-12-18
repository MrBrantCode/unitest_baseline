"""
QUESTION:
Create a function `verify_sequence` that takes two lists of the same length, `numbers` and `booleans`, as input. The function should return `True` if each number in `numbers` is even when the corresponding boolean in `booleans` is `True`, and each number is prime when the corresponding boolean is `False`. The function should return `False` otherwise.
"""

import math

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    sqrt_n = math.sqrt(n)
    for i in range(3, int(sqrt_n) + 1, 2):
        if n % i == 0:
            return False
    return True

def verify_sequence(numbers, booleans):
    for num, bool_val in zip(numbers, booleans):
        if bool_val:
            if num % 2 != 0:
                return False
        else:
            if not is_prime(num):
                return False
    return True