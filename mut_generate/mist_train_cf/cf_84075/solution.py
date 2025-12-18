"""
QUESTION:
Write a function called `is_mersenne_prime` that takes an integer `n` and checks if it's a Mersenne prime number, calculates the exponent `p` for which `2^p - 1` equals `n`, and identifies whether the derived exponent `p` is also a prime number. The function should handle edge cases or exceptions.
"""

import math

def is_prime(num):
    if num < 2:
        return False
    if num == 2 or num == 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    sqrtofnum = int(math.sqrt(num))+1
    while i <= sqrtofnum:
        if (num % i == 0) or (num % (i + 2) == 0):
            return False
        i += 6
    return True
    

def is_mersenne_prime(n):
    p = 1
    while 2 ** p - 1 <= n:
        if 2 ** p - 1 == n:
            return is_prime(p), p
        else:
            p += 1
    return False, p