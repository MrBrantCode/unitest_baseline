"""
QUESTION:
Write a function `is_prime(n)` that checks whether a given number `n` is prime or not. Use this function to print the first 1000 prime numbers. Optimize the program to minimize the time complexity of the prime number generation algorithm.
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