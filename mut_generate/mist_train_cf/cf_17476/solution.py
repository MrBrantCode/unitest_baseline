"""
QUESTION:
Create a function `find_prime_pairs(num)` that finds all pairs of prime numbers that add up to `num`. The function should return a set of tuples, where each tuple is a pair of prime numbers that add up to `num`. The pairs should be ordered such that the smaller number comes first. The function should only consider numbers from 2 to `num - 2`.
"""

import math

def find_prime_pairs(num):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

    prime_pairs = set()
    for i in range(2, num - 1):
        if is_prime(i):
            potential_second_prime = num - i
            if is_prime(potential_second_prime):
                prime_pairs.add((min(i, potential_second_prime), max(i, potential_second_prime)))
    return prime_pairs