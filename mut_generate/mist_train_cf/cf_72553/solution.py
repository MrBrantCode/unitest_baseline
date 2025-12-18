"""
QUESTION:
Create a function `create_prime_matrix(dim)` that generates a `dim x dim` matrix containing the first `dim*dim` prime numbers. Use the Sieve of Eratosthenes algorithm to efficiently generate the prime numbers and optimize the matrix creation process for speed. The function should return the prime numbers matrix as a 2D array. Note that the Sieve of Eratosthenes algorithm may need to search through a larger range of numbers to find sufficient primes, so the input `dim` should be reasonable to avoid excessive computation time.
"""

import numpy as np

def create_prime_matrix(dim):
    # Calculate n to get enough prime numbers
    n = dim*dim*dim
    # Initializing a Boolean array
    primes = [True for i in range(n+1)]
    p = 2
    while (p * p <= n):
        if (primes[p] == True):
            for i in range(p * p, n+1, p):
                primes[i] = False
        p += 1
    # Collect all prime numbers
    prime_nums = []
    for p in range(2, n):
        if primes[p]:
            prime_nums.append(p)
    # Create the prime numbers matrix
    primes_matrix = np.array(prime_nums[:dim*dim]).reshape(dim, dim)
    return primes_matrix