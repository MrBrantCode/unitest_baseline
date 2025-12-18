"""
QUESTION:
Create a function `calculate_distance_and_vector` that calculates the distance and vector components between two points in 3-dimensional space. The function should take two tuples of three integers each as input and return a tuple containing the distance rounded to two decimal places and the vector components as a tuple of three integers.
"""

import math

def calculate_distance_and_vector(point1, point2):
    """
    Calculate the distance and vector components between two points in 3-dimensional space.

    Args:
        point1 (tuple): The coordinates of the first point as a tuple of three integers.
        point2 (tuple): The coordinates of the second point as a tuple of three integers.

    Returns:
        tuple: A tuple containing the distance rounded to two decimal places and the vector components as a tuple of three integers.
    """
    distance = math.sqrt((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2 + (point2[2] - point1[2])**2)
    distance = round(distance, 2)
    vector_components = (point2[0] - point1[0], point2[1] - point1[1], point2[2] - point1[2])
    return distance, vector_components