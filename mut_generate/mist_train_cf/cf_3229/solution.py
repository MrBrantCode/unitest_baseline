"""
QUESTION:
Write a function `print_consecutive_primes(N)` that prints and returns a list of all prime numbers between 1 and a given integer N. The function should efficiently handle large values of N.
"""

import math

def print_consecutive_primes(N):
    primes = []
    for num in range(1, N + 1):
        if num < 2:
            continue
        is_prime = True
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            print(num)
            primes.append(num)
    return primes