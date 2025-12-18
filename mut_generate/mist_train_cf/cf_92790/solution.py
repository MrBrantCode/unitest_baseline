"""
QUESTION:
Create a function called `remove_primes` that takes an array of integers as input and returns a new array with all prime numbers removed. Assume the input array only contains non-negative integers.
"""

import math

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def remove_primes(arr):
    result = []
    for num in arr:
        if not is_prime(num):
            result.append(num)
    return result