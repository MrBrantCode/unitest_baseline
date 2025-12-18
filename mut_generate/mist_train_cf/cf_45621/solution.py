"""
QUESTION:
Write a function named `is_prime()` to determine whether a given number is prime. Implement a main function to generate a list of prime numbers within the range of 1 to 10,000. Then, use this list to calculate the sum of all even-indexed prime numbers and count the occurrences of twin prime pairs, which are pairs of prime numbers with a difference of 2.
"""

import math

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    sqrt_n = math.isqrt(n)
    for i in range(3, sqrt_n + 1, 2):
        if n % i == 0:
            return False
    return True