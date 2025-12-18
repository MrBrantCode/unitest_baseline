"""
QUESTION:
Construct a function `primes_squared(n)` that generates a 2D matrix of the first n odd prime numbers and their squares in ascending order, with each row containing an incremental sequence from left to right. The function should be optimized for time and space efficiency to handle large data sets. The matrix should have two columns, where the first column contains the odd prime numbers and the second column contains their squares. Note that the prime numbers should be greater than 2, as 2 is not an odd number.
"""

import numpy as np

def primes_squared(n):
    primes = []
    attempt = 3
    while len(primes) < n:
        if all(attempt % prime != 0 for prime in primes):
            primes.append(attempt)
        attempt += 2
    prime_square = [prime**2 for prime in primes]
    return np.column_stack((primes, prime_square))