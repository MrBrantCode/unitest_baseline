"""
QUESTION:
Create a function `accurate_largest_prime_factor_v2(n: float)` that calculates the largest prime factor of the absolute integer value of a given number `n`. The function should handle both positive and negative numbers, as well as decimal numbers by truncating them to integers. Assume the absolute value of `n` is greater than 1 and is not a prime number. The function should return the largest prime factor of `n` as an integer.
"""

import math

def accurate_largest_prime_factor_v2(n: float):
    n = int(abs(n))
    max_prime = -1

    while n % 2 == 0:
        max_prime = 2
        n >>= 1  

    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            max_prime = i
            n = n / i

    if n > 2:
        max_prime = n

    return max_prime