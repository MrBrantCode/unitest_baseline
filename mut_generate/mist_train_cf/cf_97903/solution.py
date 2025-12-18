"""
QUESTION:
Write a Python function named `is_prime` that determines whether a given number `n` is prime or not. Using this function, create a program to calculate the sum of the first 10 prime numbers, starting from 2 and checking each subsequent number for primality.
"""

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True