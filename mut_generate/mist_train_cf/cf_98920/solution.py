"""
QUESTION:
Implement the function `opposite_sides(a, b, c, d)` that takes four points `a`, `b`, `c`, and `d` in 2D space, where each point is represented as a tuple of `(x, y)` coordinates. The function should return `True` if `b` and `d` lie on opposite sides of `c`, considering that the angle between vectors `bc` and `cd` is acute, and the x-coordinates of `b` and `d` are within a certain limit (10 units), and `False` otherwise.
"""

import math

def opposite_sides(a, b, c, d):
    bc = [c[0] - b[0], c[1] - b[1]]
    cd = [d[0] - c[0], d[1] - c[1]]

    dot_product = bc[0] * cd[0] + bc[1] * cd[1]
    mag_bc = math.sqrt(bc[0] ** 2 + bc[1] ** 2)
    mag_cd = math.sqrt(cd[0] ** 2 + cd[1] ** 2)

    cos_angle = dot_product / (mag_bc * mag_cd)

    if cos_angle > 0 and abs(b[0] - d[0]) <= 10:
        return True

    return False