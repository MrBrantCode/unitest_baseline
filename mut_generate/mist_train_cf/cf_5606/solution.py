"""
QUESTION:
Write a function `find_closest_pair` that takes an array of points as input, where each point is a list of two numbers representing x and y coordinates. The function should find the closest pair of points in the array and return them as a tuple. The time complexity of the function should be O(n^2) and it should not use any additional data structures.
"""

import math

def find_closest_pair(points):
    n = len(points)
    min_distance = math.inf
    closest_pair = None

    for i in range(n):
        for j in range(i+1, n):
            distance = math.sqrt((points[i][0] - points[j][0])**2 + (points[i][1] - points[j][1])**2)
            if distance < min_distance:
                min_distance = distance
                closest_pair = (points[i], points[j])

    return closest_pair