"""
QUESTION:
Create a function `remove_duplicates` that takes a list of integers as input, removes duplicates, and returns a new list containing only prime numbers in ascending order.
"""

import math

def remove_duplicates(arr):
    unique_arr = list(set(arr))
    primes = [num for num in unique_arr if is_prime(num)]
    primes.sort()
    return primes

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True