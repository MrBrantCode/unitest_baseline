"""
QUESTION:
Create a function named `convert_to_polar` that takes two parameters: an array of x-coordinates and an optional array of y-coordinates. Convert the input array(s) into an array of polar coordinates, taking into account both x and y values if the y-coordinate array is provided. If the y-coordinate array is not provided or is shorter than the x-coordinate array, assume the missing y-coordinate values are 0. The function should return an array of tuples, where each tuple contains the radius and angle (in degrees) of a point in polar coordinates. The input arrays may contain up to 10^9 points.
"""

import math

def convert_to_polar(x_coords, y_coords=None):
    polar_coords = []
    n = len(x_coords)

    for i in range(n):
        x = x_coords[i]
        y = y_coords[i] if y_coords and i < len(y_coords) else 0

        r = math.sqrt(x**2 + y**2)
        theta = math.atan2(y, x)
        theta = math.degrees(theta) # Convert to degrees if desired

        polar_coords.append((r, theta))

    return polar_coords