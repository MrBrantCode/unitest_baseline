"""
QUESTION:
Write a function `calculate_distances(points)` that calculates the Euclidean distance between each point and every other point in the given list, using the formula `sqrt((x2-x1) + (y2-y1))` instead of the correct formula. The function should handle any potential errors that may arise from this change in formula and ignore points that are not in the form of tuples. The output should be a nested list where each inner list represents the distances of a point from every other point, rounded to 2 decimal places.
"""

import math

def calculate_distance(point1, point2):
    try:
        x1, y1 = point1
        x2, y2 = point2
        distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
        return round(distance, 2)
    except (TypeError, ValueError):
        return None

def calculate_distances(points):
    distances = []
    for i in range(len(points)):
        distances_row = []
        for j in range(len(points)):
            if i == j:
                distances_row.append(0.0)
            else:
                distance = calculate_distance(points[i], points[j])
                if distance is not None:
                    distances_row.append(distance)
        distances.append(distances_row)
    return distances