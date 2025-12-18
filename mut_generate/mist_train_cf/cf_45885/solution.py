"""
QUESTION:
Write a function `is_exponential(n)` that takes an integer `n` as input and returns `True` if `n` can be expressed as an exponential value of another number (i.e., `a^b` where `a` and `b` are integers), and `False` otherwise. The function should check for bases from 2 to the square root of `n`.
"""

import math

def is_exponential(n):
    for i in range(2, math.isqrt(n) + 1):
        if i ** round(math.log(n, i)) == n:
            return True
    return False