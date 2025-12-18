"""
QUESTION:
Create a function called `is_a_power_of` that takes two parameters, x and y. The function should return `True` if y is a power of x (e.g., x^n = y for some integer n) and `False` otherwise.
"""

def is_a_power_of(x, y):
    if x == y:
        return True
    if y == 1:
        return True
    if y % x != 0:
        return False
    return is_a_power_of(x, y // x)