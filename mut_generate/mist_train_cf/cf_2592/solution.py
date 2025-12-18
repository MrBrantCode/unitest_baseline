"""
QUESTION:
Create a function `find_prime_pairs` that takes an integer `num` as input and returns a set of pairs of prime numbers that add up to `num`. The pairs should be ordered in ascending order based on the first number in the pair. The input `num` will be a positive integer greater than 3. The function should have a time complexity of O(n^1.5), where n is the input number `num`.
"""

import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def find_prime_pairs(num):
    prime_pairs = set()
    for i in range(2, num - 1):
        if is_prime(i):
            j = num - i
            if is_prime(j):
                prime_pairs.add(tuple(sorted((i, j))))
    return prime_pairs