"""
QUESTION:
Write a function `find_twin_primes(start, end)` that takes two integers `start` and `end` as input and returns a list of all twin prime pairs within the given range. A twin prime pair consists of two prime numbers that differ by 2.
"""

import math

def is_prime(num):
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(num)) + 1, 2):
        if num % i == 0:
            return False
    return True

def find_twin_primes(start, end):
    twin_primes = []
    for num in range(start, end - 1):
        if is_prime(num) and is_prime(num + 2):
            twin_primes.append((num, num + 2))
    return twin_primes