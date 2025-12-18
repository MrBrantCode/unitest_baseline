"""
QUESTION:
Create a function named `power` that takes two integers, `base` and `exponent`, and calculates the result of `base` raised to the power of `exponent` without using built-in power operators. The function should return the calculated result. The input `exponent` is a non-negative integer.
"""

def power(base, exponent):
    result = 1
    for i in range(exponent):
        result = result * base
    return result