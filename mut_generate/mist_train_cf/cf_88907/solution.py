"""
QUESTION:
Write a function named `is_prime(n)` that checks if a given number `n` is prime. The function should return `True` if `n` is prime, and `False` otherwise. A prime number is a whole number greater than 1 that is divisible by only 1 and itself. The function should only check divisibility up to the square root of `n` and should only consider odd divisors for odd numbers. 

Restrictions: Use a for loop to iterate through the numbers and use a separate function to check if a number is prime.
"""

import math

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True