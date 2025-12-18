"""
QUESTION:
Write a function named `is_prime` that takes an integer `n` as input and returns a boolean indicating whether `n` is a prime number. Then use this function to print all unique 6-digit numbers where the sum of their digits is a prime number. The function should consider numbers between 100000 and 999999 inclusive.
"""

import math

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True