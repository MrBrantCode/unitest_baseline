"""
QUESTION:
Create a function `is_prime(n)` that determines whether a given number `n` is prime or not, with a time complexity of O(√n) and a space complexity of O(1). The function should return a boolean value indicating whether the number is prime.
"""

import math

def is_prime(n):
    if n < 2:
        return False

    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False

    return True