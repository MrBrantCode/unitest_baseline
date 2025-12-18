"""
QUESTION:
Create a function `find_minimum(x, y)` that takes two integers `x` and `y` as input where -10^9 <= x, y <= 10^9. The function should return the minimum of `x` and `y`. However, if either `x` or `y` is negative, return an error message "Error: Inputs cannot be negative." The function should handle cases where `x` and `y` are equal, as well as cases where `x` or `y` is at the minimum or maximum limit (-10^9 or 10^9).
"""

def find_minimum(x, y):
    if x < 0 or y < 0:
        return "Error: Inputs cannot be negative."
    else:
        return min(x, y)