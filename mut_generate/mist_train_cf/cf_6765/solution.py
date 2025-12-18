"""
QUESTION:
Create a function called `prime_factors(num)` that returns a list of all prime factors of a given number `num`. The function should be able to handle numbers up to 10^9.
"""

import math

def prime_factors(num):
    factors = []
    while num % 2 == 0:
        factors.append(2)
        num = num // 2

    for i in range(3, int(math.sqrt(num)) + 1, 2):
        while num % i == 0:
            factors.append(i)
            num = num // i

    if num > 2:
        factors.append(num)

    return factors