"""
QUESTION:
Write a function `is_prime_and_perfect_square(n)` that takes a positive integer `n` and returns `True` if `n` is both a prime number and a perfect square, and `False` otherwise. The function should have a time complexity of O(sqrt(n)) and a space complexity of O(1).
"""

import math

def is_prime_and_perfect_square(n):
    if n < 2:
        return False
    
    # Check if n is prime
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    
    # Check if n is a perfect square
    if math.isqrt(n) ** 2 != n:
        return False
    
    return True