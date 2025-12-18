"""
QUESTION:
Write a function `distance(x1, y1, x2, y2)` that calculates the Euclidean distance between two points `(x1, y1)` and `(x2, y2)` and returns the result rounded to two decimal places. The function should take four numeric arguments and return a single numeric value.
"""

import math
def distance(x1, y1, x2, y2):
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return round(distance, 2)