"""
QUESTION:
Write a function `distance(x1, y1, x2, y2)` that calculates the distance between two points with coordinates (x1, y1) and (x2, y2). The result must be accurate up to two decimal points.
"""

import math
def distance(x1, y1, x2, y2):
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return round(distance, 2)