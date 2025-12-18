"""
QUESTION:
Write a function `progressive_squares(n)` that calculates the cumulative sum of all progressive perfect squares less than `n`. A progressive number is a positive integer `n` that when divided by `d` yields a quotient `q` and a remainder `r`, and `d`, `q`, and `r` form consecutive terms of a geometric sequence. A perfect square is a number that can be expressed as the square of an integer. The function should return the sum of all progressive perfect squares less than `n`.
"""

from math import isqrt, sqrt, ceil

def progressive_squares(n):
    total = 0
    # case when n = 2q^2
    for m in range(1, isqrt(n // 2) + 1):
        for d in range(ceil(m / sqrt(2)), m + 1):
            total += 2 * m * m
            if 2 * m * m >= n: break

    # case when n = 3d^2 - k^2
    m = 2
    while True:
        for k in range(1, m):
            if (m * m - k * k) % (2 * k) == 0:
                d = (m * m - k * k) // (2 * k)
                q2 = k * k + d * d
                if d < k or q2 >= n: break
                if sqrt(q2) == isqrt(q2):
                    total += q2
        if k == 1: break
        m += 1
    return total