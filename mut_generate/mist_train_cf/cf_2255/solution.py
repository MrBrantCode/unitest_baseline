"""
QUESTION:
Write a function `find_prime_pairs(limit)` that takes an integer `limit` as input and finds all pairs of prime numbers greater than 10 such that their sum is also a prime number. The function should have a time complexity of O(n^2), where n is the number of prime numbers found, and a space complexity of O(1). The function should optimize the prime number generation to minimize the number of calculations required and handle large prime numbers efficiently.
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

def find_prime_pairs(limit):
    for p in range(10, limit+1):
        if is_prime(p):
            for q in range(p, limit-p+1):
                if is_prime(q) and is_prime(p + q):
                    print(f"({p}, {q})")