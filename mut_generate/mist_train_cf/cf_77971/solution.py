"""
QUESTION:
Create a function `prod_of_primes(arr)` that takes a one-dimensional numerical array `arr` as input and returns the product of all prime numbers within the array. The function should handle cases where there are no prime numbers in the array, in which case it should return 1.
"""

from functools import reduce
from operator import mul
import math

def prod_of_primes(arr):
    def is_prime(n):
        if n <= 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        for i in range(3, math.isqrt(n) + 1, 2):
            if n % i == 0:
                return False
        return True

    primes = [x for x in arr if is_prime(x)]
    return reduce(mul, primes, 1)