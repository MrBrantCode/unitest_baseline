"""
QUESTION:
Write a function `pow(base, exponent)` that calculates the value of `base` raised to the power of `exponent` using recursion. The function should return `base` multiplied by the result of `pow(base, exponent - 1)` until `exponent` reaches 0, at which point it should return 1.
"""

def entrance(base, exponent):
    if exponent == 0:
        return 1
    else:
        return base * entrance(base, exponent - 1)