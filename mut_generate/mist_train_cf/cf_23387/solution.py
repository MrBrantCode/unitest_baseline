"""
QUESTION:
Write a function `highest_common_factor(m, n)` that calculates and returns the highest common factor (also known as the greatest common divisor) of two given integers `m` and `n`, without using the built-in gcd function.
"""

def highest_common_factor(m, n):
    if m == 0 or n == 0:
        return 0

    a = max(m, n)
    b = min(m, n)

    while b != 0:
        a, b = b, a % b

    return a