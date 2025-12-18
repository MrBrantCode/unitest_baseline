"""
QUESTION:
Create a function `complex_diff_and_angle(num1, num2)` that calculates the absolute difference and angle between two complex numbers `num1` and `num2`. The function should return a tuple containing the absolute difference and the angle in degrees. The angle should be the difference of the phases or arguments of the two complex numbers, with respect to the positive real axis, and should be in the range from -180 to 180 degrees.
"""

import cmath
import math

def complex_diff_and_angle(num1, num2):
    abs_diff = abs(num1 - num2)
    rad_angle = cmath.phase(num1) - cmath.phase(num2)
    deg_angle = math.degrees(rad_angle)

    # Ensure angle is within -180 to 180 range
    if deg_angle > 180:
        deg_angle -= 360
    elif deg_angle < -180:
        deg_angle += 360

    return abs_diff, deg_angle