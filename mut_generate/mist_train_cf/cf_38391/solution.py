"""
QUESTION:
Given two positive integers `a` and `b`, write a function `minimize_lcm(a, b)` that returns the minimum non-negative integer `k` such that the least common multiple (LCM) of `(a + k)` and `(b + k)` is minimized. The function should take in two integers `a` and `b` as input and return the minimum `k` as output.
"""

import math

def minimize_lcm(a, b):
    a, b = min(a, b), max(a, b)
    if not b % a:
        return 0
    divs = [i for i in range(1, int(math.sqrt(b - a)) + 1) if (b - a) % i == 0]
    divs += [ (b - a) // i for i in divs if i != (b - a) // i]
    M = b * a
    k = 0
    for d in divs:
        aux_k = d * math.ceil(b / d) - b
        if math.lcm(a + aux_k, b + aux_k) < M:
            M = math.lcm(a + aux_k, b + aux_k)
            k = aux_k
    return k