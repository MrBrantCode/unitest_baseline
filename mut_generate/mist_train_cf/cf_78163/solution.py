"""
QUESTION:
Compose a function `power(base, exp)` that calculates the result of `base` raised to the power of `exponent` without using Python's built-in power function or any looping constructs. The function should be optimized to handle cases where the exponent is a very large number.
"""

def power(base, exp):
    if exp == 0:
        return 1
    elif exp % 2 == 0:   # For even powers
        sqrt_result = power(base, exp // 2)
        return sqrt_result * sqrt_result
    else:                 # For odd powers
        return base * power(base, exp - 1)