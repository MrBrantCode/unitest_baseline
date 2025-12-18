"""
QUESTION:
Write a function `convert_to_polar` that takes a 2D array of points in Cartesian coordinates as input and returns an array of polar coordinates. Each point in the input array is represented as `[x, y]`. The function should return an array of polar coordinates where each point is represented as `[r, θ]`, with `r` being the radius and `θ` being the angle in radians. Assume the input array can contain up to 10^9 points.
"""

import math

def convert_to_polar(points):
    """
    Convert an array of points in Cartesian coordinates to an array of polar coordinates.

    Args:
        points (list): A 2D array of points in Cartesian coordinates, where each point is represented as [x, y].

    Returns:
        list: An array of polar coordinates, where each point is represented as [r, θ].
    """
    polar_coordinates = []
    for point in points:
        x, y = point
        radius = math.sqrt(x**2 + y**2)
        angle = math.atan2(y, x)
        polar_coordinates.append([radius, angle])
    return polar_coordinates