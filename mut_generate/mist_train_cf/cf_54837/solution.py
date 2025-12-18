"""
QUESTION:
Implement a function named `power` that takes two parameters, `base` and `exponent`, both integers. Calculate the exponentiation of `base` raised to the power of `exponent` without using the default exponentiation functions or operators. Assume `exponent` is a non-negative integer.
"""

def power(base, exponent):
    result = 1
    for _ in range(exponent):
        result *= base
    return result