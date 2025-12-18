"""
QUESTION:
Write a function `calculateTotalDistance` that takes a string of coordinates in the format "x1-y1,x2-y2,x3-y3..." as input and returns the total distance traveled when moving from the first point to the last point in the given order. The distance between two points (x1, y1) and (x2, y2) is calculated using the Euclidean distance formula: distance = sqrt((x2 - x1)^2 + (y2 - y1)^2).
"""

import math

def calculateTotalDistance(coordinates: str) -> float:
    points = coordinates.split(',')
    total_distance = 0.0
    for i in range(len(points) - 1):
        x1, y1 = map(float, points[i].split('-'))
        x2, y2 = map(float, points[i + 1].split('-'))
        distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        total_distance += distance
    return total_distance