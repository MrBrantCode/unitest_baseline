"""
QUESTION:
Write a Python function named `modInv(a, p)` that calculates the modular multiplicative inverse of `a` modulo `p`, where `a` and `p` are integers. The function should return `None` if either `a` or `p` is a square of a prime number. Implement the function using the extended Euclidean algorithm. Assume that the inputs `a` and `p` are valid integers.
"""

import math

def is_square(n):
    return math.isqrt(n) ** 2 == n

def is_prime(n):
    if n <= 1 or (n % 2 == 0 and n > 2): 
        return False
    return all(n % i for i in range(3, int(math.sqrt(n)) + 1, 2))

def is_square_of_prime(n):
    root = math.isqrt(n)
    return is_square(n) and is_prime(root)

def extended_euclidean(a, b):
    if a == 0:
        return b, 0, 1
    else:
        gcd, x, y = extended_euclidean(b % a, a)
        return gcd, y - (b // a) * x, x

def modInv(a: int, p: int):
    if is_square_of_prime(a) or is_square_of_prime(p):
        return None
    gcd, x, y = extended_euclidean(a, p)
    return x % p