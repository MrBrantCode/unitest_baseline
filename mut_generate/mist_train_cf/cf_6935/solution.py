"""
QUESTION:
Write a function `power(base, exponent)` that calculates the result of `base` raised to the power of `exponent`. The function should handle large values of `exponent` efficiently and return the result as a decimal with a precision of at least 50 decimal places. Both `base` and `exponent` are integers, and `base` is positive. The function should also handle negative values of `exponent`.
"""

from decimal import Decimal, getcontext

def entrance(base, exponent):
    getcontext().prec = 50
    
    if exponent == 0:
        return Decimal(1)
    
    if exponent < 0:
        return Decimal(1) / entrance(base, -exponent)
    
    result = Decimal(1)
    while exponent > 0:
        if exponent & 1:
            result *= Decimal(base)
        base *= base
        exponent >>= 1
    
    return result