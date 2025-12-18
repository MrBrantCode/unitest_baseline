"""
QUESTION:
Write a function `sum_of_squares_of_primes` that takes an array of 16-bit unsigned integers as input and returns the sum of the squares of the first 50 prime numbers found in the array. The function should stop searching for prime numbers once it has found 50 primes or has checked all elements in the array. The result should be a floating point number.
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
    for i in range(len(arr)):
        if is_prime(arr[i]):
            primes.append(arr[i])
            if len(primes) == 50:
                break
    sum_of_squares = sum([p**2 for p in primes])
    return sum_of_squares