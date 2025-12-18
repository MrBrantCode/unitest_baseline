"""
QUESTION:
Create a function `modInv(a: int, p: int)` that computes and returns the modular inverse of `a` under modulo `p`. However, if both `a` and `p` are squares of a prime number, the function should return `None`. The function should work for integers `a` and `p` in the range `1 <= a, p <= 10^9`, where `p` is a prime number.
"""

import math

def modInv(a: int, p: int):
    def is_square(n):
        return n == math.isqrt(n) ** 2

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

    if is_square_of_prime(a) and is_square_of_prime(p):
        return None

    gcd, x, y = extended_euclidean(a, p)
    return x % p