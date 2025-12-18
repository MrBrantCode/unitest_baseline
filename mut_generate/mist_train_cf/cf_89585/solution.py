"""
QUESTION:
Create a function named `prime_factors(num)` that takes an integer `num` as input and returns a list of its prime factors. The input number can be as large as 10^9. The function should find all prime factors of the given number and return them in a list.
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