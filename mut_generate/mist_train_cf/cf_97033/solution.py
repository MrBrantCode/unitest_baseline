"""
QUESTION:
Define a function `power(base, exponent)` that calculates the value of `base` raised to the power of `exponent`, where `base` and `exponent` are integers greater than 1. The function should handle negative exponents by returning the reciprocal of the result. The function should not use any built-in exponentiation or logarithmic functions and should have a time complexity of O(log(n)), where n is the absolute value of `exponent`.
"""

def power(base, exponent):
    if exponent == 0:
        return 1
    elif exponent < 0:
        return 1 / power(base, -exponent)
    elif exponent % 2 == 0:
        return power(base * base, exponent // 2)
    else:
        return base * power(base * base, (exponent - 1) // 2)