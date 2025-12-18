"""
QUESTION:
Implement a function `sum_of_square(c)` that takes a non-negative integer `c` as input and returns the pair of integers `a` and `b` such that `a^2 + b^2 = c`. If multiple pairs exist, return the pair where `a` and `b` are the largest. If no such pair exists, return an empty array. The constraints are `0 <= c <= 2^31 - 1` and `-2^31 <= a, b <= 2^31 - 1`.
"""

import math

def entrance(c):
    left = 0
    right = math.isqrt(c)

    while left <= right:
        current = left * left + right * right
        if current < c:
            left += 1
        elif current > c:
            right -= 1
        else:
            return [left, right]
    return []