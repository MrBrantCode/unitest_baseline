"""
QUESTION:
Create a function called `max_prime_difference` that takes an array of positive integers as input and returns the maximum difference between two prime numbers in the array. The array will always contain at least two prime numbers.
"""

import math

def max_prime_difference(arr):
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

    primes = [num for num in arr if is_prime(num)]
    return max(primes) - min(primes)