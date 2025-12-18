"""
QUESTION:
Write a function called `calculate_distance` that takes in two lists of 5 integers each representing points in a 5D coordinate system and returns the Euclidean distance between the two points, rounded to the nearest integer. The function should use the Euclidean distance formula: d = sqrt((x2 - x1)^2 + (y2 - y1)^2 + (z2 - z1)^2 + (w2 - w1)^2 + (v2 - v1)^2).
"""

import math

def calculate_distance(point1, point2):
    return round(math.sqrt(sum((a - b) ** 2 for a, b in zip(point1, point2))))