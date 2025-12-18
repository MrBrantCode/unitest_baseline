"""
QUESTION:
Create a function named `find_primes` that takes an array of integers as input and returns an array containing all prime numbers from the input array. The function should consider negative integers as prime if their absolute values are prime, and exclude non-integer and non-prime numbers.
"""

import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def find_primes(arr):
    primes = []
    for num in arr:
        if isinstance(num, int) or isinstance(num, float):
            if is_prime(abs(int(num))):
                primes.append(num)
    return primes