"""
QUESTION:
Implement a recursive function `f(x)` that calculates the value of the polynomial expression `x^3 + 4x^2 + 5x + 6`. The function should take an integer `x` as input, handle negative values of `x` by returning a custom error message "Invalid input", and return the computed value for non-negative `x`.
"""

def f(x):
    if x < 0:
        return "Invalid input"
    elif x == 0:
        return 6
    else:
        return x * (x * (x + 4) + 5) + 6