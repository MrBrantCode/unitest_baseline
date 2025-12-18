"""
QUESTION:
Create a function `prime_factors(num)` that takes a positive integer `num` up to 10^12 and returns the smallest prime factor of the number.
"""

import math

def smallest_prime_factor(num):
    if num % 2 == 0:
        return 2

    for i in range(3, int(math.sqrt(num)) + 1, 2):
        if num % i == 0:
            return i

    return num