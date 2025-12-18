"""
QUESTION:
Write a function `prime_factors(n)` that takes an integer `n` as input and returns a list of its prime factors. The function should have a time complexity of approximately O(sqrt(n)) to ensure optimal efficiency for large inputs.
"""

import math

def prime_factors(n):
    factors = []

    while n % 2 == 0:
        factors.append(2)
        n = n / 2

    for i in range(3, int(math.sqrt(n))+1, 2):
        while n % i == 0:
            factors.append(i)
            n = n / i

    if n > 2:
        factors.append(int(n))

    return factors