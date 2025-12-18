"""
QUESTION:
Implement a function `calculate_distance(x1, y1, x2, y2)` to calculate the Euclidean distance between two points (x1, y1) and (x2, y2) in a 2D plane, where the distance is given by the formula: distance = sqrt((x2 - x1)^2 + (y2 - y1)^2). The function should return the calculated distance. The input coordinates (x1, y1, x2, y2) are integers or floats, and the function should handle these data types.
"""

import math

def calculate_distance(x1, y1, x2, y2):
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return distance