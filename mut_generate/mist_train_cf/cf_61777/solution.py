"""
QUESTION:
Write a function `is_strong_right_truncatable_harshad_prime(n)` that checks whether a given number `n` is a strong, right truncatable Harshad prime or not. The function should return `True` if `n` is a strong, right truncatable Harshad prime, and `False` otherwise. A strong, right truncatable Harshad prime is a prime number such that when its last digit is recursively truncated, it consistently results in a Harshad number, and when divided by the sum of its digits, it yields a prime number.
"""

import math

def is_prime(n):
    if n == 1: return False
    if n == 2 or n == 3: return True
    if n % 2 == 0 or n % 3 == 0: return False
    i = 5
    w = 2
    while i * i <= n:
        if n % i == 0: return False
        i += w
        w = 6 - w
    return True

def is_harshad(num):
    return num % sum(int(i) for i in str(num)) == 0

def is_strong_right_truncatable_harshad_prime(n):
    if is_prime(n):
        trunc = n
        while trunc:
            if not is_harshad(trunc):
                return False
            trunc //= 10
        return is_prime(n // sum(int(i) for i in str(n)))
    return False