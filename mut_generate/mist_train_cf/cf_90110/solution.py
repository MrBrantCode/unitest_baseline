"""
QUESTION:
Define a function `power(base, exponent)` that calculates the power of a positive integer base raised to the power of an integer exponent with a time complexity of O(log(n)) where n is the absolute value of the exponent. The function should not use any built-in exponentiation or logarithmic functions. It should handle both positive and negative exponents, returning the reciprocal of the result for negative exponents.
"""

def power(base, exponent):
    if exponent == 0:
        return 1
    if exponent == 1:
        return base
    if exponent < 0:
        return 1 / power(base, -exponent)
    
    result = 1
    current_base = base
    
    while exponent > 0:
        if exponent % 2 == 1:
            result *= current_base
        current_base *= current_base
        exponent //= 2
    
    return result