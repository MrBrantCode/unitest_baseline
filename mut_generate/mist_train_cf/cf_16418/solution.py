"""
QUESTION:
Write a function named `prime_factorization` that takes an integer `n` as input and returns a list of its prime factors. The function should run in O(sqrt(n)) time complexity and use O(1) space complexity, excluding the space required for the output list.
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