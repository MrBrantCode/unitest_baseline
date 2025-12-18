"""
QUESTION:
Implement a function `sort_numbers(numbers)` that takes a list of integers as input and returns a new list where prime numbers are sorted in descending order and non-prime numbers are sorted in descending order and placed at the beginning of the output list. 

The function should utilize an optimized primality test, such as checking divisibility up to the square root of a number.
"""

import math

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    sqrt_n = int(math.sqrt(n)) + 1
    for i in range(3, sqrt_n, 2):
        if n % i == 0:
            return False
    return True

def sort_numbers(numbers):
    primes = []
    non_primes = []
    for num in numbers:
        if is_prime(num):
            primes.append(num)
        else:
            non_primes.append(num)
    return sorted(primes, reverse=True) + sorted(non_primes, reverse=True)