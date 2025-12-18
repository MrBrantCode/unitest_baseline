"""
QUESTION:
Implement a function `power(base, exponent)` that calculates the power of the base raised to the power of the exponent. The function should have a time complexity of O(log(n)), where n is the value of the exponent, and should not use any built-in exponentiation or logarithmic functions. The base and exponent values will be positive integers greater than 1, or negative integers for the exponent, in which case the function should return the reciprocal of the result.
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