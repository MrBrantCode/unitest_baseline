"""
QUESTION:
Write a function `power(base, exponent)` that calculates the result of `base` raised to the power of `exponent` efficiently, handling large values of `exponent` and returning the result as a decimal with a precision of at least 10 decimal places. The function should take two positive integers as input, `base` and `exponent`, where `exponent` can be negative.
"""

def power(base, exponent):
    if exponent == 0:
        return 1
    
    result = 1
    abs_exponent = abs(exponent)
    
    while abs_exponent > 0:
        if abs_exponent % 2 == 1:
            result *= base
        base *= base
        abs_exponent //= 2
    
    if exponent < 0:
        result = 1 / result
    
    return round(result, 10)