"""
QUESTION:
Design a function `generate_prime_squares(limit)` that generates a sequence of prime numbers, each of which is the sum of two perfect squares, and whose product equals a perfect cube, up to the given `limit`. The function should return the sequence of prime numbers and find the smallest and largest numbers in the sequence. The function should only consider prime numbers, perfect squares, and perfect cubes.
"""

import math

def is_perfect_cube(n):
    return round(n ** (1/3)) ** 3 == n

def generate_prime_squares(limit):
    primes = []
    for i in range(2, limit):
        is_prime = True
        for j in range(2, int(math.sqrt(i)) + 1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            for a in range(1, int(math.sqrt(i)) + 1):
                for b in range(a, int(math.sqrt(i)) + 1):
                    if a**2 + b**2 == i and is_perfect_cube(i * a**2 * b**2):
                        primes.append(i)
    return primes