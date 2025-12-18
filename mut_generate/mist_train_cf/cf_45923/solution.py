"""
QUESTION:
Create a function named `find_closest_point` that takes two parameters: a point and a list of points, where each point is represented as a list of two integers (x-coordinate and y-coordinate). The function should return the point in the list that is closest to the given point. The distance between two points is calculated using the Euclidean distance formula.
"""

import math

def find_closest_point(point, points):
    # Define a helper function that calculates the distance between two points
    def calculate_distance(point1, point2):
        return math.sqrt(((point1[0] - point2[0]) ** 2) + ((point1[1] - point2[1]) ** 2))

    # Initialize the closest distance to be the distance between the given point and the first point in the list
    closest_distance = calculate_distance(point, points[0])
    # Initialize the closest point to be the first point in the list
    closest_point = points[0]

    for p in points:
        # If the distance between the given point and the current point is less than the closest distance
        if calculate_distance(point, p) < closest_distance:
            # Update the closest distance and the closest point
            closest_distance = calculate_distance(point, p)
            closest_point = p

    return closest_point