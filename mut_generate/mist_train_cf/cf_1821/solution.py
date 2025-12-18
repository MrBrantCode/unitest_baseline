"""
QUESTION:
Create a function `is_prime(n)` that checks whether a given integer `n` is prime or not. The function should return `True` if the number is prime and `False` otherwise. Use this function to print all prime numbers from 1 to 100000 and also state whether each number is prime or not. The function should be efficient and handle large numbers.
"""

import math

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True