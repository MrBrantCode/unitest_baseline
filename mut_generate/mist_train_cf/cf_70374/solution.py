"""
QUESTION:
Design a function `find_prime_quadruplets` that takes two integers `start` and `end` as input, representing a range of numbers, and returns all prime quadruplets within this range. A prime quadruplet is a set of four prime numbers of the form (n, n+2, n+6, n+8). The function should be optimized to handle large ranges efficiently.
"""

import math

def find_prime_quadruplets(start, end):
    quadruplets = []
    for i in range(start, end - 5, 2):
        if (i <= 1 or i % 2 == 0) or (i+2 <= 1 or (i+2) % 2 == 0) or (i+6 <= 1 or (i+6) % 2 == 0) or (i+8 <= 1 or (i+8) % 2 == 0):
            continue
        sqrt_i = math.isqrt(i)
        sqrt_i_plus_2 = math.isqrt(i+2)
        sqrt_i_plus_6 = math.isqrt(i+6)
        sqrt_i_plus_8 = math.isqrt(i+8)
        is_i_prime = True
        is_i_plus_2_prime = True
        is_i_plus_6_prime = True
        is_i_plus_8_prime = True
        for j in range(3, max(sqrt_i, sqrt_i_plus_2, sqrt_i_plus_6, sqrt_i_plus_8) + 1, 2):
            if i % j == 0:
                is_i_prime = False
            if (i+2) % j == 0:
                is_i_plus_2_prime = False
            if (i+6) % j == 0:
                is_i_plus_6_prime = False
            if (i+8) % j == 0:
                is_i_plus_8_prime = False
        if is_i_prime and is_i_plus_2_prime and is_i_plus_6_prime and is_i_plus_8_prime:
            quadruplets.append((i, i+2, i+6, i+8))
    return quadruplets