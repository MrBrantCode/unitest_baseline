"""
QUESTION:
Create a function `opposite_sides(a, b, c, d)` that takes four points represented as tuples of (x, y) coordinates and returns `True` if points `b` and `d` lie on opposite sides of point `c`, and `False` otherwise. The function should check if the angle between vectors `bc` and `cd` is acute, and if the x-coordinates of `b` and `d` are within 10 units of each other.
"""

import math

def opposite_sides(a, b, c, d):
    # Calculate the vectors bc and cd
    bc = [c[0] - b[0], c[1] - b[1]]
    cd = [d[0] - c[0], d[1] - c[1]]
    
    # Calculate the dot product of bc and cd
    dot_product = bc[0] * cd[0] + bc[1] * cd[1]
    
    # Calculate the magnitude of bc and cd
    mag_bc = math.sqrt(bc[0] ** 2 + bc[1] ** 2)
    mag_cd = math.sqrt(cd[0] ** 2 + cd[1] ** 2)
    
    # Calculate the cosine of the angle between bc and cd
    cos_angle = dot_product / (mag_bc * mag_cd)
    
    # Check if the angle is acute
    if cos_angle > 0:
        # Check if the x-coordinates of b and d are within certain limits
        if abs(b[0] - d[0]) <= 10:
            return True
    
    return False