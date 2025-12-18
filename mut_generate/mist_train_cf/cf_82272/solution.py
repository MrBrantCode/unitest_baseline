"""
QUESTION:
Create a function `log_base_n` that takes two parameters `n` and `x`, both of which are real numbers. The function should calculate the logarithm base `n` of `x` using the change of base formula. The function should handle edge cases where `n` or `x` is less than or equal to 0, and return an error message in such cases.
"""

import math

def log_base_n(n, x):
    # Check if n and x are both greater than 0
    if n > 0 and x > 0:
        # Calculate log base n using the change of base formula
        return math.log(x) / math.log(n)
    else:
        return "Cannot calculate logarithm for zero or negative numbers."