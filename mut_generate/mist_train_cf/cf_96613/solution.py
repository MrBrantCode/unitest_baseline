"""
QUESTION:
Write a function `power(base, exponent)` that calculates the result of `base` raised to the power of `exponent` efficiently for both large positive and negative `exponent` values, returning the result as a decimal with a precision of at least 10 decimal places.
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