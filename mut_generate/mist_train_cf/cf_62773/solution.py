"""
QUESTION:
Create a function named `total_distance` that takes a list of 3D coordinate tuples as input and returns the total Euclidean distance traveled by moving from the first coordinate to the last in the given order, passing through each intermediate coordinate. The function should be able to handle any number of coordinate tuples in the list.
"""

import math

def total_distance(points):
    total_distance = 0
    for i in range(len(points)-1):
        total_distance += math.sqrt((points[i][0]-points[i+1][0])**2 + (points[i][1]-points[i+1][1])**2 + (points[i][2]-points[i+1][2])**2)
    return total_distance