"""
QUESTION:
Write a function named `isPrime` that takes an integer `n` and returns a boolean indicating whether `n` is a prime number. The function should return `false` if `n` is less than 2. For optimization, the function should only check for divisors up to the square root of `n`.
"""

import math

def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True