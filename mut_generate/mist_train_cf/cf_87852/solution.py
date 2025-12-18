"""
QUESTION:
Develop a function named `print_consecutive_primes` that takes an integer `N` as input and prints all prime numbers between 1 and `N`. The function should also return a list of these prime numbers. The function should be efficient enough to handle large values of `N`.
"""

import math

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def print_consecutive_primes(N):
    primes = [num for num in range(1, N + 1) if is_prime(num)]
    for prime in primes:
        print(prime)
    return primes