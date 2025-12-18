"""
QUESTION:
Write a function named `generate_matrix(size)` to generate a square matrix filled with zeros. The size of the matrix must be a prime number. If the size is not a prime number, return None.
"""

import math

def is_prime(n):
    """Check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def generate_matrix(size):
    """Generate a matrix filled with zeros, where size is a prime number."""
    if not is_prime(size):
        return None
    
    return [[0] * size for _ in range(size)]