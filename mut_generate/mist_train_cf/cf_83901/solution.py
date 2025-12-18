"""
QUESTION:
Implement a function `power(base, exponent)` that calculates the value of `base` raised to the power of `exponent` using only basic arithmetic operations (+, -, *, /). The function should handle cases where `exponent` is negative.
"""

def power(base, exponent):
    if exponent == 0:
        return 1
    if exponent < 0:
        base = 1/base
        exponent = -exponent
    result = 1
    for _ in range(exponent):
        result *= base
    return result