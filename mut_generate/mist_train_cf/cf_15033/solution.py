"""
QUESTION:
Create a function `find_primes(n)` that generates an array of all prime numbers between 2 and `n`, inclusive. The function should take an integer `n` as input and return a list of integers. The list should contain all prime numbers in the range from 2 to `n` in ascending order. The input `n` will be a positive integer.
"""

import math

def find_primes(n):
    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                return False
        return True

    primes = [i for i in range(2, n + 1) if is_prime(i)]
    return primes