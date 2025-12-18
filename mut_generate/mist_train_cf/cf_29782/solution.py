"""
QUESTION:
Write a function `calculateDistances` that takes a 2D array of points as input, where each point is represented by its x and y coordinates in the format [[x1, y1], [x2, y2], ... [xn, yn]]. The function should return a new 2D array containing the distances of each point from the origin (0, 0), calculated using the formula distance = sqrt(x^2 + y^2).
"""

import math

def calculateDistances(points):
    distances = []
    for point in points:
        x, y = point
        distance = math.sqrt(x**2 + y**2)
        distances.append([round(distance, 15), round(distance, 15)])  # Rounding to 15 decimal places
    return distances