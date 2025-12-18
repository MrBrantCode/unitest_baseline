"""
QUESTION:
Write a function named `is_prime(n)` that checks whether a given positive integer `n` is a prime number or not. The function should return `True` if `n` is prime and `False` otherwise. The input `n` is a positive integer greater than 1.
"""

def is_prime(n):
    # check if n is divisible by any number between 2 and n-1 
    for i in range (2, n):
        # if a number is divisible, then return False
        if (n % i == 0):
            return False
    # if n is only divisible by itself, return True
    return True