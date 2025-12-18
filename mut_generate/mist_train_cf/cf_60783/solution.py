"""
QUESTION:
Write a function called `calculate_lcm_of_primes` that calculates the Least Common Multiple (LCM) of all prime numbers up to a specified limit. The function should be able to handle both small and large prime numbers efficiently. The input to the function is an integer `limit` representing the upper limit for prime numbers, and the output is the LCM of all prime numbers up to the given limit.
"""

import numpy as np

def calculate_lcm_of_primes(limit):
    primes = np.ones(limit+1, dtype=bool)

    primes[:2] = False
    N_max = int(np.sqrt(len(primes) - 1))

    for ind in range(2, N_max + 1):
        if primes[ind]:
            primes[ind**2::ind] = False

    primes = np.nonzero(primes)[0]
    lcm = 1
    for i in primes:
        lcm = lcm*i//np.gcd(lcm, i)
    return lcm