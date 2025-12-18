"""
QUESTION:
Write a function `generate_prime_numbers(n)` that generates the first `n` prime numbers and groups them sequentially into sub-arrays of 20, maintaining the original order of appearance. The function should return a 2D array where each sub-array contains 20 prime numbers.
"""

import numpy as np

def generate_prime_numbers(n):
    """
    Generate and group the first n prime numbers into sub-arrays of 20
    """
    def is_prime(num):
        if num < 2:
            return False
        if num == 2:
            return True
        if num % 2 == 0:
            return False
        max_divisor = int(num**0.5) + 1
        for d in range(3, max_divisor, 2):
            if num % d == 0:
                return False
        return True

    primes = []
    i = 0
    while len(primes) < n:
        if is_prime(i):
            primes.append(i)
        i += 1

    return np.array(primes).reshape(-1, 20)