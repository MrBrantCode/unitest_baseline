"""
QUESTION:
Write a function `greatest_prime(arr)` that takes an array of integers as input and returns the greatest prime number in the array. The function should consider the absolute values of the numbers in the array and return None if the array is empty or does not contain any prime numbers.
"""

import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def greatest_prime(arr):
    primes = [x for x in arr if is_prime(abs(x))]
    if not primes:
        return None
    return max(primes)