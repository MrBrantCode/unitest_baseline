"""
QUESTION:
Write a function `is_prime()` to check if a number is prime. Then, use this function to print all prime numbers between 0 and 10^7 in ascending order. The input range is inclusive of the end value (10^7).
"""

import math

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True