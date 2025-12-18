"""
QUESTION:
Write a function `power(base, exponent)` that calculates the result of a positive integer `base` raised to the power of a positive integer `exponent`. The function should handle large values of `exponent` efficiently.
"""

def power(base, exponent):
    result = 1
    while exponent > 0:
        if exponent % 2 == 1:  # if the current bit is 1
            result *= base
        base *= base  # square the base
        exponent //= 2  # divide the exponent by 2
    return result