"""
QUESTION:
Write a function called `prime_lcm_upto` that calculates the least common multiple (LCM) of all prime numbers up to a given integer `n`. The function should return the calculated LCM. The input `n` is a positive integer.
"""

import math

def prime_lcm_upto(n):
    """Calculates the LCM of all prime numbers upto n."""
    def is_prime(num):
        """Check if a number is prime."""
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def lcm(a, b):
        """Calculate the least common multiple of two numbers."""
        return a * b // math.gcd(a, b)

    primes = [i for i in range(2, n + 1) if is_prime(i)]
    result = 1
    for prime in primes:
        result = lcm(result, prime)
    return result