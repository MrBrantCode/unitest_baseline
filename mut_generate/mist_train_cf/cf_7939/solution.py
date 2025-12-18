"""
QUESTION:
Write a function called `print_twin_primes(n)` that prints all pairs of twin prime numbers below a given number `n`. Twin prime numbers are prime numbers that differ by 2. The function should achieve a time complexity of O(sqrt(n)) and should not use any built-in mathematical or prime number functions or libraries, except for the square root calculation. The function should only use a single loop to find the twin prime numbers.
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
    for i in range(2, n-2, 2):
        if is_prime(i) and is_prime(i + 2):
            twin_primes.append((i, i+2))
    for twin_prime in twin_primes:
        print(twin_prime)