"""
QUESTION:
Create a function called `is_prime` that checks if a given number is prime or not without using built-in prime-checking functions or libraries. The function must have a time complexity of O(log(n)) where n is the given number. The function should handle very large numbers efficiently without running out of memory or exceeding time limits.
"""

import math

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    sqrt_n = int(math.sqrt(n)) + 1
    for divisor in range(3, sqrt_n, 2):
        if n % divisor == 0:
            return False
    return True