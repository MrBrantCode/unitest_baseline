"""
QUESTION:
Design a function `calculate_distance` to calculate the distance between two points in 3-D space, where each point is represented as a tuple of three integers (x, y, z) representing the coordinates along the x, y, and z axes. The function should return the distance as a floating-point number rounded to two decimal places.
"""

import math

def calculate_distance(p1, p2):
    x1, y1, z1 = p1
    x2, y2, z2 = p2
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)
    return round(distance, 2)