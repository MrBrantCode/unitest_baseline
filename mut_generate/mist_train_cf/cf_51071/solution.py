"""
QUESTION:
Create a function named `is_prime(n)` that takes a number `n` as input and returns a boolean value indicating whether the number is prime or not. The function should be able to handle large numbers efficiently. The input `n` can be any integer. The function should return `False` for numbers less than or equal to 1.
"""

import math

def is_prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True