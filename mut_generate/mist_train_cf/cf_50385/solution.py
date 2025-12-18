"""
QUESTION:
Write a function that takes an integer range defined by a start and end value as input, and prints all prime numbers within that range. The function should efficiently check for primes and handle edge cases such as negative numbers and the numbers 0 and 1. The function should be able to handle large ranges. The function should take user input for the start and end values. The function should be named `is_prime` and should be used within a loop to check each number in the range.
"""

import math

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    sqrt_n = math.isqrt(n)
    for i in range(3, sqrt_n + 1, 2):
        if n % i == 0:
            return False
    return True