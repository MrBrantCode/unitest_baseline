"""
QUESTION:
Write a function called `least_common_multiple` that takes a positive integer `n` as input and returns the smallest multiple shared by every prime number up to `n`.
"""

import math

def least_common_multiple(n):
    def is_prime(i):
        if i <= 1 or (i % 2 == 0 and i > 2): 
            return False
        for j in range(3, int(math.sqrt(i)) + 1, 2):
            if i % j == 0:
                return False
        return True

    result = 1
    for i in range(2, n + 1):
        if is_prime(i):
            p = i
            while (p * i <= n):
                p *= i
            result *= p
    return result