"""
QUESTION:
Write a function `calculate_distances(coordinates)` that takes a list of strings representing coordinates in the format "x y" and returns a list of distances of each coordinate from the origin, rounded to two decimal places.
"""

import math

def calculate_distances(coordinates):
    return [round(math.sqrt(x**2 + y**2), 2) for x, y in (map(int, coord.split(' ')) for coord in coordinates)]