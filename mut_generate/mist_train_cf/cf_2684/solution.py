"""
QUESTION:
Write a function called `find_primes` that takes a list of integers as input and returns a new list containing only the prime numbers from the original list. The function should have a time complexity of O(n*sqrt(m)), where n is the length of the input list and m is the maximum value in the list.
"""

import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def find_primes(numbers):
    primes = [number for number in numbers if is_prime(number)]
    return primes