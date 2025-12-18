"""
QUESTION:
Write a function `prime_factorization(n)` that finds the prime factorization of a given integer `n` with a time complexity of O(sqrt(n)) and a space complexity of O(1). The function should return a list of prime factors of `n`.
"""

import math

def prime_factorization(n):
    factors = []
    
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    
    factor = 3
    while factor * factor <= n:
        while n % factor == 0:
            factors.append(factor)
            n //= factor
        factor += 2
    
    if n > 1:
        factors.append(n)
    
    return factors