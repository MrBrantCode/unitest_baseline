"""
QUESTION:
Write a function prime_factorization(n) that finds the prime factorization of a given number n. The function should run in O(log(log(n))) time complexity and use O(1) space complexity, handling numbers up to 10^12 efficiently. It should return a list of prime factors.
"""

import math

def prime_factorization(n):
    factors = []

    # Check if n is divisible by 2
    while n % 2 == 0:
        factors.append(2)
        n //= 2

    # Check for odd prime factors
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            factors.append(i)
            n //= i

    # If n is still greater than 1, it means n is a prime number
    if n > 1:
        factors.append(n)

    return factors