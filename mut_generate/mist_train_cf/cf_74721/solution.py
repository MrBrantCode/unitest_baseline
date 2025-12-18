"""
QUESTION:
Create a function `generate_primes(n)` that efficiently generates and stores all prime numbers not exceeding a given integer `n`, balancing storage optimization and expeditious data retrieval. The function should return an array of prime numbers. Note that `n` is a large number, up to 1 million.
"""

import numpy as np

def generate_primes(n):
    is_prime = np.ones((n,), dtype=bool)
    is_prime[:2] = 0  # 0 and 1 are not primes
    N_max = int(np.sqrt(len(is_prime)))+1   # loop until sqrt(n)

    for j in range(2, N_max):
        is_prime[j*j::j] = False

    return np.nonzero(is_prime)[0]