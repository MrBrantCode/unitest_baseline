"""
QUESTION:
Write a function named `sum_of_squares_of_primes` that takes an array of 16-bit unsigned integers as input and returns the sum of the squares of the first 50 prime numbers found in the array.
"""

import math

def sum_of_squares_of_primes(arr):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(math.sqrt(n))+1):
            if n % i == 0:
                return False
        return True

    primes = []
    for num in arr:
        if is_prime(num):
            primes.append(num)
            if len(primes) == 50:
                break
    return sum([p**2 for p in primes])