"""
QUESTION:
Create a function `calculate_distance` that calculates the distance between two points in three-dimensional space. The function should take two tuples of three integers each as input, representing the coordinates of the two points. The function should return the distance between the two points as a floating-point number. The solution should not use the standard distance formula or any mathematical functions or libraries. The time complexity of the solution should be O(1).
"""

import math

def calculate_distance(point1, point2):
    return math.sqrt((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2 + (point2[2] - point1[2])**2)