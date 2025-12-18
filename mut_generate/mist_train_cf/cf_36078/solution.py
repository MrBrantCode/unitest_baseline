"""
QUESTION:
Implement a function `calculate_power(k, l)` that takes two integers `k` and `l` as input and returns the smallest integer `r` such that `k` raised to the power of `r` is greater than or equal to `l`.
"""

def calculate_power(k, l):
    r = 1
    while k ** r < l:
        r += 1
    return r