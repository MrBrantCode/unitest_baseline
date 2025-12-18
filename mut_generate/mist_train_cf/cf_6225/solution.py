"""
QUESTION:
Create a function `is_power_of(x, y)` that takes two parameters, `x` and `y`, and returns a boolean value. The function should return `True` if `y` is a power of `x`, and `False` otherwise. Both `x` and `y` must be positive integers; if either is not, the function should return `False`.
"""

def is_power_of(x, y):
    if x <= 0 or not isinstance(x, int) or isinstance(x, float):
        return False
    if y <= 0 or not isinstance(y, int) or isinstance(y, float):
        return False
    if x == 1:
        return y == 1
    power = 0
    while y % x == 0:
        y = y / x
        power += 1
    return y == 1