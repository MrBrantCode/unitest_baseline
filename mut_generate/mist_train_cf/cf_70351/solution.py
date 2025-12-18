"""
QUESTION:
Given a positive integer `n`, write a function `T(n)` to determine the count of necklace triplets `(a, b, c)` where `a`, `b`, and `c` are positive integers, and `b` does not exceed `n`. A triplet `(a, b, c)` is a necklace triplet if it's possible to position `k >= 3` unique circles tangent to each other and to two given circles `C_in` and `C_out` with diameters `XY` and `WZ` respectively, where `X`, `Y`, `Z`, and `W` are points on the same straight line with distances `a`, `b`, and `c` between them. 

The function `T(n)` should return the total count of such unique necklace triplets.
"""

from bisect import bisect_right

def T(n):
    max_a = 2 * int(((n * n / (n + 1) + n) // 1) ** 0.5)
    sq_cplus = [i * i for i in range(max_a + 1)]
    res = 0
    for b in range(1, n + 1):
        for a in range(1, b + 1):
            res += bisect_right(sq_cplus, a * b + a * a + b * b) - b
    return res