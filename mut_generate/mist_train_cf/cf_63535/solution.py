"""
QUESTION:
Write a function `calculate_power(x, y, z)` that calculates the value of `x` to the power `y` modulo `z` using the `pow(x, y, z)` function. The function should handle the case where `z` is zero without throwing an error.
"""

def calculate_power(x, y, z):
    if z != 0:
        return pow(x, y, z)
    else:
        return "z cannot be zero"