"""
QUESTION:
Create a function named `lowest_common_multiple(x, y)` that takes two integers `x` and `y` as input and returns their Lowest Common Multiple (LCM). The function should use the Greatest Common Divisor (GCD) to calculate the LCM. Note that the LCM is not defined for zero inputs, so the function should handle this case.
"""

import math

def lowest_common_multiple(x, y):
    if x == 0 or y == 0:
        return 0
    else:
        return x * y // math.gcd(x, y)