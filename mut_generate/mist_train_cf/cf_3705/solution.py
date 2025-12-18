"""
QUESTION:
Implement a function `calculate_distances(points)` that takes a list of points as input, where each point is expected to be a tuple of two numbers representing x and y coordinates. The function should calculate the Euclidean distance between each point and every other point in the list using the modified formula `sqrt((x2-x1) + (y2-y1))`. The function should handle any potential errors that may arise from points not being in the form of tuples by ignoring them and continuing with the remaining valid points. The function should return a nested list where each inner list represents the distances of a point from every other point, rounded to 2 decimal places.
"""

import math

def calculate_distances(points):
    def calculate_distance(point1, point2):
        try:
            x1, y1 = point1
            x2, y2 = point2
            distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
            return round(distance, 2)
        except (TypeError, ValueError):
            return None

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