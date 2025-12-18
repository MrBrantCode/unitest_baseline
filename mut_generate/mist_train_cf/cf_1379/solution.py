"""
QUESTION:
Create a function `is_prime(n)` that checks whether a given number `n` is a prime number. The function should have a time complexity of O(sqrt(n)) and a space complexity of O(1).
"""

import math

def entrance(n):
    if n <= 1:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0:
        return False

    max_divisor = math.isqrt(n) + 1
    for divisor in range(3, max_divisor, 2):
        if n % divisor == 0:
            return False
    return True