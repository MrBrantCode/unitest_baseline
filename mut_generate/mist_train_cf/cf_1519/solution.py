"""
QUESTION:
Write a Python function named `is_prime` that takes a positive integer `n` as input and returns a list of all prime numbers between `n` and the smallest prime number larger than `n`. The function should use a trial division method to check for primality and handle inputs up to 10^9.
"""

import math

def is_prime(n):
    def is_divisible(num):
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                return True
        return False

    primes = []
    next_prime = n + 1
    while True:
        if not is_divisible(next_prime):
            primes.append(next_prime)
            break
        next_prime += 1

    return primes