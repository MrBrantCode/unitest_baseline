"""
QUESTION:
Write a function named `power` that calculates the power of the base number raised to the power of the exponent number. The function should have a time complexity of O(log(n)) where n is the value of the exponent. Do not use any built-in exponentiation or logarithmic functions.
"""

def power(base, exponent):
    result = 1
    while exponent > 0:
        if exponent % 2 == 1:  # If exponent is odd
            result *= base
        base *= base
        exponent //= 2
    return result