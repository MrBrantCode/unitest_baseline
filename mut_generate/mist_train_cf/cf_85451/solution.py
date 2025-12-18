"""
QUESTION:
Write a Python function called `primes_up_to` that takes a positive integer `n` as input, checks if each number from 1 to `n` is prime, and prints those that are. Use a helper function called `is_prime` to check for primality. The `is_prime` function should return `True` if its input is prime, and `False` otherwise. Assume that the input `n` is a non-negative integer.
"""

import math

def is_prime(n):
    '''Check if a number is prime'''
    if n == 1 or n == 0:
        return False
    for i in range(2,int(math.sqrt(n))+1):
        if n%i == 0:
            return False
    return True

def primes_up_to(n):
    '''Print all primes up to a given number'''
    for i in range(1,n+1):
        if is_prime(i):
            print(i)