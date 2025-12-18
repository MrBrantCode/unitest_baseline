"""
QUESTION:
Create a function `distance_to_vesica` that takes in the x and y coordinates of a point and the radii of two circles with the same center at the origin (0, 0). The function should return the distance from the point to the vesica piscis shape formed by the intersection of the two circles.
"""

import math

def distance_to_vesica(point_x, point_y, radius1, radius2):
    distance_to_origin = math.sqrt(point_x**2 + point_y**2)
    
    if distance_to_origin <= abs(radius1 - radius2):
        return abs(distance_to_origin - abs(radius1 - radius2))
    else:
        return abs(distance_to_origin - (radius1 + radius2) / 2)