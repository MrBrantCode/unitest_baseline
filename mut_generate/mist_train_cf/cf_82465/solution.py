"""
QUESTION:
Implement a function `shortest_path_3D` that takes a list of 3-dimensional points as input and returns the total sum of distances from the origin point to each point in the order that minimizes the total travel distance, along with the optimal sequence of points to travel. The origin point is assumed to be (0, 0, 0). The function should calculate the distance between two points using Pythagoras Theorem. The function does not need to return to the start point. The input list of points is not empty and contains at least one point. The points are represented as tuples of three integers.
"""

import itertools
import math

def calculate_distance(point1, point2):
    return math.sqrt((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2 + (point2[2] - point1[2])**2)

def shortest_path_3D(points):
    points = [(0, 0, 0)] + points
    min_distance = float('inf')
    shortest_path = None
    
    for path in itertools.permutations(points[1:]):
        path = [points[0]] + list(path)
        
        total_distance = sum(calculate_distance(path[i], path[i + 1]) for i in range(len(path) - 1))
        
        if total_distance < min_distance:
            min_distance = total_distance
            shortest_path = path
            
    return min_distance, shortest_path[1:]