"""
QUESTION:
Create a function `power` that takes a decimal number `base` and an exponent as input, calculates `base` raised to the power of the exponent, and returns the result. The `base` should be within the range of -100 to 100, inclusive; otherwise, return an error message. The exponent will be rounded to the nearest integer if it is not already an integer. The function should have a time complexity of O(log N) or better.
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