"""
QUESTION:
Create a function named `is_prime` that takes an integer `n` as input and returns a boolean indicating whether `n` is a prime number. The function should have a time complexity of O(sqrt(n)).
"""

import math

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    sqrt_n = int(math.sqrt(n)) + 1
    for i in range(3, sqrt_n, 2):
        if n % i == 0:
            return False
    return True