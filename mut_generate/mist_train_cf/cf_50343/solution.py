"""
QUESTION:
Create a function `is_prime(num)` that determines if a number is prime. The function should correctly handle numbers less than 2, and it should only check divisibility up to the square root of the number. Use this function to create another function `filter_primes(arr)` that filters a given array and returns a list of prime numbers. The function should handle arrays of any length, including empty and one-element arrays, and it should correctly process negative numbers and zeroes.
"""

import math

def entrance(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True