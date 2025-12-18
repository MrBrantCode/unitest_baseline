"""
QUESTION:
Create a function called `prime_numbers` that takes an integer `n` as input and returns a list of all prime numbers up to `n` in ascending order. The function should have a time complexity of O(n*sqrt(m)), where `n` is the input integer and `m` is the largest number being checked for primality.
"""

import math

def prime_numbers(n):
    primes = []
    for num in range(2, n + 1):
        if all(num % i != 0 for i in range(2, int(math.sqrt(num)) + 1)):
            primes.append(num)
    return primes