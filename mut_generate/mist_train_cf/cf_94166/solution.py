"""
QUESTION:
Create a function called `sum_of_primes` that takes an integer `n` as input and returns a tuple containing the sum of all prime numbers from 2 to `n` and a list of all prime numbers within that range.
"""

import math

def is_prime(num):
    """
    Function to check if a number is prime.
    """
    if num <= 1:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def sum_of_primes(n):
    """
    Function to find the sum of all prime numbers from 2 to n and return a list of prime numbers within that range.
    """
    primes = []
    prime_sum = 0
    for num in range(2, n + 1):
        if is_prime(num):
            primes.append(num)
            prime_sum += num
    return prime_sum, primes