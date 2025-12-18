"""
QUESTION:
Write a function named `calculate_distance` that calculates the distance between two points given their coordinates. The distance between two points (x1, y1) and (x2, y2) is given by the formula: distance = sqrt((x2 - x1)^2 + (y2 - y1)^2). The function should take two tuples (x, y) as input and return the calculated distance. The function must use the math library to calculate the square root.
"""

import math

def calculate_distance(coord1, coord2):
    x1, y1 = coord1
    x2, y2 = coord2
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)