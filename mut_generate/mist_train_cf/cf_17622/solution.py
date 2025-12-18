"""
QUESTION:
Write a function called `extract_last_n_primes` that takes a list of positive integers and an integer `n` as input, and returns the last `n` unique prime numbers from the list in the order they appear from the end of the list.
"""

import math

def extract_last_n_primes(lst, n):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                return False
        return True

    primes = set()
    for num in reversed(lst):
        if is_prime(num):
            primes.add(num)
        if len(primes) == n:
            break
    return list(reversed(list(primes)))