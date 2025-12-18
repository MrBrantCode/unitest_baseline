"""
QUESTION:
Write a function named `generate_matrix` that generates a square matrix filled with zeros, where the size of the matrix is a prime number. The function should take an integer as input and return the generated matrix if the input is a prime number, otherwise it should return `None`.
"""

import math

def generate_matrix(size):
    """Generate a matrix filled with zeros, where size is a prime number."""
    if size < 2:
        return None
    for i in range(2, int(math.sqrt(size)) + 1):
        if size % i == 0:
            return None
    
    matrix = [[0] * size for _ in range(size)]
    return matrix