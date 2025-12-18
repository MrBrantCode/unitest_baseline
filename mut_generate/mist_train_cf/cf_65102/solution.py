"""
QUESTION:
Write a function `C(n)` that takes an integer `n` as input and returns the number of pairs of positive integers `a` and `b` such that `a * b = n`, `a <= b`, and `a` and `b` have the same number of divisors. The function should be able to handle large inputs, such as `n = 100!`. The number of divisors of a number `n` can be calculated using the formula `d(n) = (e1 + 1) * (e2 + 1) * ... * (ek + 1)`, where `ei` are the exponents of the prime factors of `n`.
"""

import math

def num_factors(n):
    factors = []
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return len(set(factors))

def C(n):
    count = 0
    sqrt_n = math.isqrt(n)
    for i in range(1, sqrt_n+1):
        if n % i == 0:
            if num_factors(i) == num_factors(n//i):
                count += 1
    return count