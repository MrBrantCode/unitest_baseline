"""
QUESTION:
Create a function `power` that takes two parameters: `base` and `exponent`. The function should raise `base` to the power of `exponent` and return the result. The `base` must be within the range -100 to 100, inclusive; if not, return an error message. The `exponent` should be an integer, but if it's not, it should be rounded to the nearest integer. The function should handle decimal numbers and negative exponents, and it should have a time complexity of O(log N) or better.
"""

def power(base, exponent):
    if not (-100 <= base <= 100):
        return "Error: Number is out of range."
    
    if not isinstance(exponent, int):
        exponent = round(exponent)
    
    result = 1
    
    if exponent < 0:
        base = 1 / base
        exponent = -exponent
    
    while exponent:
        if exponent & 1:
            result *= base
        base *= base
        exponent >>= 1
    
    return result