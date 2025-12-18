"""
QUESTION:
Write a function named `print_odd_indexed_prime_numbers` that takes a list of integers as input. The function should print a list of numbers that are located at odd indices in the input list and are prime numbers. The function should be optimized to handle large input lists efficiently.
"""

import math

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    sqrtn = math.sqrt(n)
    for divisor in range(3, int(sqrtn) + 1, 2):
        if n % divisor == 0:
            return False
    return True

def print_odd_indexed_prime_numbers(lst):
    primes = [lst[i] for i in range(1, len(lst), 2) if is_prime(lst[i])]
    print(primes)