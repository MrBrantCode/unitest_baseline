"""
QUESTION:
Write a function named `power` that takes two parameters: a positive integer `base` and an integer `exponent`. The function should calculate the result of `base` raised to the power of `exponent`, handling large values of `exponent` efficiently and negative values of `exponent` by returning the result as a decimal with a precision of at least 50 decimal places.
"""

from decimal import Decimal, getcontext

def power(base, exponent):
    # Set the precision of decimal calculations to at least 50 decimal places
    getcontext().prec = 50
    
    # Handle the case when exponent is zero
    if exponent == 0:
        return Decimal(1)
    
    # Handle the case when exponent is negative
    if exponent < 0:
        return Decimal(1) / power(base, -exponent)
    
    result = Decimal(1)
    while exponent > 0:
        # If the current bit of exponent is 1, multiply the result by base
        if exponent & 1:
            result *= Decimal(base)
        # Square the base and divide the exponent by 2
        base *= base
        exponent >>= 1
    
    return result