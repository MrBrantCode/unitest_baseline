"""
QUESTION:
Create a function "prime_factorization" that takes an integer as input and returns a list of its prime factors in ascending order without any duplicates. The function should be able to handle large numbers efficiently, specifically numbers up to 10^18.
"""

import math

def prime_factorization(n):
    factors = set()
    for i in range(2, int(math.sqrt(n)) + 1):
        while n % i == 0:
            factors.add(i)
            n //= i
    if n > 1:
        factors.add(n)
    return sorted(list(factors))