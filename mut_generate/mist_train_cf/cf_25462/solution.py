"""
QUESTION:
Create a function named `num_permutations` that takes an integer `n` as input and returns the number of valid permutations of length `n` with respect to a given set of `n` distinct elements. The function should use the mathematical concept of factorial to calculate the result.
"""

import math

def num_permutations(n):
    if n == 0:
        return 0
    else:
        return math.factorial(n)