"""
QUESTION:
Create a function `is_power_of(x, y)` that takes two parameters, x and y, and returns True if y is a power of x. The function should only consider x and y as valid inputs if they are positive integers, returning False for negative numbers, non-integer values, and non-integer decimal numbers.
"""

def entrance(x, y):
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