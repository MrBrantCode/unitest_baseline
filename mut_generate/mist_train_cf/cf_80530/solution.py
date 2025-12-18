"""
QUESTION:
Write a function `count_primes` that recursively counts the number of prime numbers in a two-dimensional array of integers. The function should return the total count of prime numbers. Each sub-array can contain integers from 2 to N, where N is any positive integer. Use recursion in your solution.
"""

import math

def is_prime(n):
    """ Helper function to check if a number is prime"""
    if n < 2:
        return False      
    for i in range(2, math.isqrt(n) + 1):
        if n % i == 0:
            return False
    return True

def count_primes(arr):
    """ Recursive function to count the number of primes in a 2D array """
    if len(arr) == 0:
        return 0
    else:
        # Recursively divides the 2D array into smaller 1D arrays, then sums up the results.
        return count_primes(arr[:-1]) + sum(is_prime(x) for x in arr[-1])