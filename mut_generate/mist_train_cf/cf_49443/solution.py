"""
QUESTION:
Write a function `find_exponent(n)` that determines if a given positive integer `n` can be expressed as the result of an exponentiation operation (`base^exponent`) where `base` is a prime number. The function should return the `base` and `exponent` if such a representation exists; otherwise, it should return `None`. The function should be able to handle relatively small integers due to potential computational complexity and integer overflow issues. If multiple prime number bases exist for a single value, the function should return the smallest one.
"""

import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def find_exponent(n):
    for i in range(2, n):
        if is_prime(i): 
            j = 1
            while(i ** j <= n):
                if i ** j == n:
                    return i, j 
                j += 1
    return None