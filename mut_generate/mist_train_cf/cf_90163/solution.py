"""
QUESTION:
Create a function `print_twin_primes(n)` that prints all pairs of twin prime numbers below a given number `n`, where twin primes are prime numbers that differ by 2. The function should achieve a time complexity of O(sqrt(n)) and only use a single loop. The solution should not use any built-in mathematical or prime number functions or libraries, with the exception of `math.sqrt` for calculating square roots.
"""

import math

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def print_twin_primes(n):
    twin_primes = []
    for i in range(2, n-1, 2):
        if is_prime(i) and is_prime(i + 2):
            twin_primes.append((i, i+2))
    for twin_prime in twin_primes:
        print(twin_prime)