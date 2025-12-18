"""
QUESTION:
Create a function named `prime_factors` that takes a single positive integer `n` as input. The function should return a list of prime factors of `n` if `n` is not a prime number, and a message indicating that `n` has no prime factors other than itself if `n` is a prime number. The function should have a time complexity of O(sqrt(n)).
"""

import math

def prime_factors(n):
    factors = []

    for i in range(2, int(math.sqrt(n)) + 1):
        while n % i == 0:
            factors.append(i)
            n /= i

    if n > 1:
        factors.append(int(n))

    if len(factors) == 0:
        return f"{n} is a prime number and has no prime factors other than itself."
    else:
        return factors