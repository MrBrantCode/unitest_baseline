"""
QUESTION:
Create a function `distance` that calculates the Euclidean distance between two points in a 2D space. Then create another function, let's call it `find_nearest_points`, that uses the `distance` function to find the two nearest points in a given set of points. The `find_nearest_points` function should take a list of points, where each point is a tuple of two integers, and return the two nearest points along with the distance between them. The function should have a time complexity of O(n^2) where n is the number of points.
"""

import math

def find_nearest_points(points):
    def distance(point1, point2):
        return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

    min_distance = float('inf')
    point1 = point2 = None

    for i in range(len(points)):
        for j in range(i+1, len(points)):
            dist = distance(points[i], points[j])
            if dist < min_distance:
                min_distance = dist
                point1, point2 = points[i], points[j]
                
    return (point1, point2, min_distance)