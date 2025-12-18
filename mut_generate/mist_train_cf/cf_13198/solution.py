"""
QUESTION:
Create a function `convert_to_polar_coordinates` that takes an array of points, where each point is represented by a tuple of its x and y coordinates. The function should convert each point to polar coordinates (radius and angle in radians) and return the array of polar coordinates. The input array can contain up to 10^6 points.
"""

import math

def convert_to_polar_coordinates(points):
    polar_coordinates = []
    
    for point in points:
        x, y = point
        radius = math.sqrt(x**2 + y**2)
        angle = math.atan2(y, x)
        polar_coordinates.append((radius, angle))
    
    return polar_coordinates