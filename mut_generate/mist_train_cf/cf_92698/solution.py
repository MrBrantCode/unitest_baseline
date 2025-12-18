"""
QUESTION:
Create a function `is_power(x, y)` that takes two parameters, `x` and `y`. The function should return `True` if `y` is a power of `x`, and `False` otherwise. Both `x` and `y` must be positive integers.
"""

def is_power(x, y):
    if x <= 0 or y <= 0 or not isinstance(x, int) or not isinstance(y, int):
        return False

    power = 0
    while x ** power <= y:
        if x ** power == y:
            return True
        power += 1
    return False