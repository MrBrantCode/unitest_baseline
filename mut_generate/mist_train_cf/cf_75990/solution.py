"""
QUESTION:
Create a function `prime_matrix(n)` that takes an integer `n` as input and returns a 2D array (matrix) containing the first `n` prime numbers. The prime numbers should be arranged in a column (i.e., a matrix with one column and `n` rows).
"""

import numpy as np

def prime_matrix(n):
    primes = []
    candidate = 2
    while len(primes) < n:
        if all(candidate % prime != 0 for prime in primes):
            primes.append(candidate)
        candidate += 1
    return np.array(primes).reshape(-1, 1)