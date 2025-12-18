"""
QUESTION:
Implement a function `rotate_point` that takes the coordinates of a point (`x`, `y`), the coordinates of a pivot point (`xi`, `yi`), and a rotation angle in degrees (`angle`) as input. Return a tuple containing the new coordinates of the point after rotating it around the pivot point by the given angle.
"""

import math

def rotate_point(x, y, xi, yi, angle):
    x_no_offset = x - xi
    y_no_offset = y - yi
    new_x = xi + x_no_offset * math.cos(math.radians(angle)) - y_no_offset * math.sin(math.radians(angle))
    new_y = yi + x_no_offset * math.sin(math.radians(angle)) + y_no_offset * math.cos(math.radians(angle))
    return (new_x, new_y)