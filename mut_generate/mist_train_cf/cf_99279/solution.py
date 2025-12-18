"""
QUESTION:
Design an algorithm for the function `generate_prime_squares(limit)` that generates a sequence of prime numbers, each of which is the sum of two perfect squares, and whose product equals a perfect cube. The function should return the sequence of prime numbers and also find the smallest and largest numbers in the sequence. The function should only consider prime numbers up to the given limit.
"""

import math

def is_perfect_cube(n):
    return round(n ** (1. / 3)) ** 3 == n

def generate_prime_squares(limit):
    primes = set()
    for i in range(2, limit):
        if all(i % j != 0 for j in range(2, int(math.sqrt(i)) + 1)):
            for a in range(1, int(math.sqrt(i)) + 1):
                b = math.sqrt(i - a ** 2)
                if b == int(b) and is_perfect_cube(i * a**2 * int(b)**2):
                    primes.add(i)
    return sorted(list(primes))