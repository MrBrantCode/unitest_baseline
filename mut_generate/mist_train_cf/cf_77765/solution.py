"""
QUESTION:
Create two functions: `factorial(n)` and `is_prime(num)`. The `factorial(n)` function should calculate the factorial of a given number `n` using recursion. The `is_prime(num)` function should determine whether a given number `num` is prime or not, applying the most efficient algorithm possible to optimize performance for large inputs.
"""

import math

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def is_prime(num):
    if num == 1:
        return False
    elif num == 2:
        return True
    elif num > 2 and num % 2 == 0:
        return False
    else:
        for i in range(3, math.isqrt(num) + 1, 2):
            if num % i == 0:
                return False
        return True