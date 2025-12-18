"""
QUESTION:
Write a function `convert_to_polar_coordinates(points)` that converts an array of Cartesian coordinates to an array of polar coordinates. The input array `points` contains up to 10^6 tuples, each representing a point in Cartesian coordinates (x, y). Return an array of tuples, where each tuple contains the radius and angle in radians of the corresponding point in polar coordinates.
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