"""
QUESTION:
Write a function named 'perfect_squares_cubes' that takes an integer 'n' as input and returns the count of perfect squares and perfect cubes between 1 and 'n'. The function should also correctly classify between a 'perfect square' and a 'perfect cube' and count numbers that are both a perfect square and a perfect cube once for both categories. Optimize the algorithm to reduce the number of checks.
"""

import math

def perfect_squares_cubes(n):
    """
    Returns the count of perfect squares and perfect cubes between 1 and 'n'.

    Args:
        n (int): The upper limit.

    Returns:
        tuple: A tuple containing the count of perfect squares and perfect cubes.
    """

    # List of perfect squares
    perfect_squares = [i**2 for i in range(1, int(math.sqrt(n))+1)]
    
    # List of perfect cubes
    perfect_cubes = [i**3 for i in range(1, int(n**(1./3))+1) if i**3 <= n]
    
    return len(perfect_squares), len(perfect_cubes)