"""
QUESTION:
Implement a function `log_exp1p` that calculates the natural logarithm of 1 plus the input value using a specific transformation. The function should take a numerical input `x` and return the natural logarithm of 1 plus `x` if `x` is greater than or equal to 0, or the natural logarithm of `explin(x)` if `x` is less than 0. The `explin` function is defined as `explin(x) = 1 + x` if `x >= 0`, and `explin(x) = exp(x)` if `x < 0`.
"""

import numpy as np

def log_exp1p(x: float) -> float:
    return np.where(x >= 0, np.log1p(x), np.log(np.where(x >= 0, 1 + x, np.exp(x))))