"""
QUESTION:
Write a function `num_paths(n)` that calculates the number of paths from the top-left corner to the bottom-right corner of an `n x n` grid, where the only permissible movements are to the right and downwards, and returns this count. The function should use combinatorics to solve the problem.
"""

import math

def num_paths(n):
    # calculate C(2n, n)
    return math.factorial(2*n) // (math.factorial(n)**2)