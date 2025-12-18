"""
QUESTION:
Write a function `H(m, n)` that calculates the sum of `G(a, b)` for all `1 <= a <= m` and `1 <= b <= n`, where `G(a, b)` is the smallest non-negative integer `n` such that the greatest common divisor of `(n^3 + b)` and `((n + a)^3 + b)` achieves its maximum value. The function `H(m, n)` should be able to handle large inputs of `m` and `n`, and it should be optimized for performance.
"""

from math import gcd
from functools import lru_cache

@lru_cache(maxsize=None)
def G(a, b):
    max_gcd, max_n = -1, -1
    for n in range(b + 2):
        current_gcd = gcd(n * n * n + b, (n + a) * (n + a) * (n + a) + b)
        if current_gcd > max_gcd:
            max_gcd, max_n = current_gcd, n
    return max_n

def entrance(m, n):
    total = 0
    for a in range(1, m + 1):
        for b in range(1, n + 1):
            total += G(a, b)
    return total