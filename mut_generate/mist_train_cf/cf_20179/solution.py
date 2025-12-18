"""
QUESTION:
Implement a function `power(base, exponent)` to calculate the value of `base` raised to the power of `exponent` without using any built-in functions or libraries for exponentiation. The function should be optimized for time complexity to handle large exponents (e.g., in the range of 10^9 or higher).
"""

def power(base, exponent):
    result = 1
    while exponent > 0:
        if exponent % 2 == 1:
            result *= base
        exponent //= 2
        base *= base
    return result