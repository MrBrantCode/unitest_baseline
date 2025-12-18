"""
QUESTION:
Create a function `remove_primes` that takes an array of integers as input and returns a new array with all prime numbers removed. The function should use a helper function `is_prime` to check if a number is prime. The `is_prime` function should return True if the number is prime and False otherwise.
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