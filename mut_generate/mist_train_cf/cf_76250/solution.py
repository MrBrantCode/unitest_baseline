"""
QUESTION:
Write a function `prime_factorial_sum(n)` that calculates the sum of the factorials of the first `n` prime numbers. The function should return the sum of these factorials. Note that the input `n` is a positive integer.
"""

import math

def is_prime(n):
    """Check if the number n is prime or not."""
    if n == 2 or n == 3:
        return True
    if n < 2 or n%2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def prime_factorial_sum(n):
    """Find the sum of the factorials of the first n primes."""
    prime_sum = 0
    prime_count = 0
    i = 2
    while prime_count < n:
        if is_prime(i):
            prime_sum += math.factorial(i)
            prime_count += 1
        i += 1
    return prime_sum