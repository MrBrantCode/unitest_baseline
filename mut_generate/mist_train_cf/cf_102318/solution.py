"""
QUESTION:
Write a function `second_smallest_prime` that takes a list of distinct positive integers with at least 10 elements as input and returns the second smallest prime number. The function should be able to handle lists of up to 10,000 elements efficiently.
"""

import math

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def second_smallest_prime(numbers):
    unique_numbers = list(set(numbers))
    primes = [n for n in unique_numbers if is_prime(n)]
    primes.sort()
    return primes[1]