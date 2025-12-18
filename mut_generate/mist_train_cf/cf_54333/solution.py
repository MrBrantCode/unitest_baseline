"""
QUESTION:
Define a function `golden_section(n, a, b)` that calculates the worst-case cost `C(n, a, b)` achieved by an optimal strategy for the given values of `n`, `a`, and `b` in a game of numerical hide-and-seek, where `n` is the range of the set of integers, `a` is the cost of guessing too low, and `b` is the cost of guessing too high. Then, use this function to compute the sum of `C(10^12, sqrt(k), sqrt(F_k))` for `1 ≤ k ≤ 30`, where `F_k` is the `k`th Fibonacci number, and provide the result rounded to 8 decimal places.
"""

import math

def calculate_worst_case_cost(n, a, b):
    R = 0.6180339887498949
    C = 1.3819660112501051
    p = q = 1
    p1 = q1 = 0

    while True:
        if a * p + b * q < a * p1 + b * q1 or p + q > n:
            return a * p1 + b * q1
        p1, q1 = p, q
        p, q = C * p + R * q, R * p + C * q