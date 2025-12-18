"""
QUESTION:
Write a function `sum_of_cubed_primes(n)` to calculate the sum of the cube of prime numbers from 1 to a given positive integer `n`. The function should return the sum of the cubes of all prime numbers in the range 1 to `n`.
"""

import math

def sum_of_cubed_primes(n):
    return sum([i**3 for i in range(1, n + 1) if all(i % j != 0 for j in range(2, int(math.sqrt(i)) + 1)) and i > 1])