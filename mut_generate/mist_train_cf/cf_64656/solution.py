"""
QUESTION:
Write a function called `primes_in_array` that takes an array of integers as input and returns an array of booleans. Each boolean value in the output array should indicate whether the corresponding number in the input array is a prime number (True) or not (False). The function should handle integers outside the usual range of prime numbers, including negative numbers, zero, and one. Optimize the function for performance to handle large arrays and large numbers efficiently.
"""

import numpy as np

def primes_in_array(array):
    def is_prime(n):
        if n < 2:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        max_divisor = int(np.sqrt(n))
        for d in range (3, 1 + max_divisor, 2):
            if n % d == 0:
                return False
        return True

    return [is_prime(x) for x in array]