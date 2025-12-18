"""
QUESTION:
Write a function `find_max_distance_pair` that takes a list of 2D points as input and returns the pair of points with the maximum Euclidean distance between them. The input list will contain at least two points, and each point is represented as a list of two numbers.
"""

import math

def find_max_distance_pair(data):
    def calculate_distance(point1, point2):
        x1, y1 = point1
        x2, y2 = point2
        return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

    max_distance = 0
    max_distance_pair = None
    for i in range(len(data)):
        for j in range(i+1, len(data)):
            distance = calculate_distance(data[i], data[j])
            if distance > max_distance:
                max_distance = distance
                max_distance_pair = (data[i], data[j])
    return max_distance_pair