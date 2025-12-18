"""
QUESTION:
Implement a function called `power(base, exponent)` that takes a base number and an exponent as input and returns the result of raising the base to the power of the exponent. The function should have a time complexity of O(log n), where n is the exponent.
"""

def power(base, exponent):
    result = 1
    while exponent > 0:
        if exponent % 2 == 1:
            result *= base
        base *= base
        exponent //= 2
    return result