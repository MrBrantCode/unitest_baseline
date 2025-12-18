"""
QUESTION:
Define a function `power(base, exponent)` that calculates the value of `base` raised to the power of `exponent` without using built-in exponentiation or logarithmic functions. The function should handle both positive and negative integer exponents greater than -1, and have a time complexity of O(log(n)), where n is the absolute value of the exponent.
"""

def entance(base, exponent):
    if exponent == 0:
        return 1
    elif exponent < 0:
        return 1 / entance(base, -exponent)
    elif exponent % 2 == 0:
        return entance(base * base, exponent // 2)
    else:
        return base * entance(base * base, (exponent - 1) // 2)