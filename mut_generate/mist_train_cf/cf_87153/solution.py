"""
QUESTION:
Write a function `is_prime(n)` that checks if a given number `n` is prime or not. The function should return `True` if the number is prime and `False` otherwise. Then, use this function to print all prime numbers from 1 to 100,000, and also print a message stating whether each number is prime or not.
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