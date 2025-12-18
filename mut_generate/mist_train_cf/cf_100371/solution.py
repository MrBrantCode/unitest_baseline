"""
QUESTION:
Design a function `generate_prime_squares(limit)` that generates a sequence of prime numbers up to the given limit, where each prime number is the sum of two perfect squares and the product of the prime number, the two perfect squares is a perfect cube. The function should return the sequence of prime numbers, the smallest prime number in the sequence, and the largest prime number in the sequence. The limit should be a positive integer, and the function should only consider prime numbers greater than 2.
"""

import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def is_perfect_cube(n):
    return round(n ** (1./3)) ** 3 == n

def generate_prime_squares(limit):
    primes = []
    for i in range(3, limit, 2):
        if is_prime(i):
            for a in range(1, int(math.sqrt(i)) + 1):
                for b in range(a, int(math.sqrt(i)) + 1):
                    if a**2 + b**2 == i and is_perfect_cube(i * a**2 * b**2):
                        primes.append(i)
    if primes:
        return primes, min(primes), max(primes)
    else:
        return [], None, None