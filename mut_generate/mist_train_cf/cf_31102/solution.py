"""
QUESTION:
Write a function `calculate_f` that takes four input parameters: `x`, `y`, `z`, and `pi`. The function should calculate the value of the expression `(1 + 3*pi2)*cos(z)*sin(x)*sin(y)`, where `pi2` is the square of `pi`, and `cos(z)`, `sin(x)`, and `sin(y)` are the cosine and sine of the angles `z`, `x`, and `y` in radians, respectively. The function should return the calculated value.
"""

import math

def calculate_f(x, y, z, pi):
    pi2 = pi ** 2
    f_2 = (1 + 3 * pi2) * math.cos(z) * math.sin(x) * math.sin(y)
    return f_2