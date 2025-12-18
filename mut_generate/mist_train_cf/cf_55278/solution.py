"""
QUESTION:
Write a function T(M) that calculates the sum of N(u^3/v^3) for all ordered pairs of mutually prime positive integers (u, v) not exceeding M, where N(r) is the least positive integer n for which s(n) = r * n and s(n) denotes the integer that results from transposing the leftmost digit of the decimal representation of n to the rightmost position. The result should be returned modulo 1,000,000,007.
"""

from math import gcd
from fractions import Fraction as F
MOD = int(1e9 + 7)

def T(M):
    sp = [0] * (M + 1)
    def N(n):
        s = n // 10 + n % 10 * (10 ** (len(str(n)) - 1))
        return s

    for v in range(1, M + 1):
        sp[v] = sp[v - 1]
        v3 = pow(v, 3, MOD)
        for u in range(v - 1, 0, -1):
            if gcd(u, v) == 1:
                r = F(pow(u, 3, MOD), v3)
                n = (10 * r.numerator - 1) // r.denominator + 1
                s = n if n % 10 != 0 else n - 1
                if r * s == N(n):
                    sp[v] = (sp[v] + n) % MOD
    return sp[M]