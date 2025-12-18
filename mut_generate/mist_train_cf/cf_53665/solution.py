"""
QUESTION:
Write a function named `primes_and_sum` that accepts a list of integers as input. The function should return a tuple containing a list of all prime numbers from the input list and the sum of these prime numbers. The function should have a time complexity better than O(n) by only checking divisibility up to the square root of the numbers.
"""

from math import isqrt

def primes_and_sum(lst):
    def is_prime(n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    primes = [x for x in lst if is_prime(x)]
    return primes, sum(primes)