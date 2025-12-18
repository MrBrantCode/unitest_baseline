"""
QUESTION:
Write a function named `is_prime` that checks whether a given number `n` is prime or not. Then, using the `is_prime` function, create a loop that prints the first 1000 prime numbers, starting from 2. The loop should be optimized to minimize time complexity by only checking divisibility up to the square root of `n`.
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