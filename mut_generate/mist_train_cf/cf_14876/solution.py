"""
QUESTION:
Create a function named `prime_factors(n)` that generates a list of all prime factors for a given positive integer `n`, excluding the number itself. The function should also return the count of prime factors and the sum of all prime factors.
"""

import math

def entrance(n):
    factors = []
    count = 0
    total = 0

    # Check if n is divisible by 2
    while n % 2 == 0:
        factors.append(2)
        count += 1
        total += 2
        n = n // 2

    # Check for odd prime factors
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            factors.append(i)
            count += 1
            total += i
            n = n // i

    # If n is a prime number greater than 2
    if n > 2:
        factors.append(n)
        count += 1
        total += n

    return factors, count, total