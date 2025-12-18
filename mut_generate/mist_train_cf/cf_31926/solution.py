"""
QUESTION:
Write a function `find_shortest_distance` that takes a list of 3D points as input, where each point is represented as a tuple of three coordinates (x, y, z), and returns a tuple containing the two points that are closest to each other and the distance between them. If there are multiple pairs with the same shortest distance, return the first pair encountered.
"""

import math

def find_shortest_distance(points):
    min_distance = float('inf')
    closest_pair = ()
    
    for i in range(len(points)):
        for j in range(i+1, len(points)):
            dist = math.sqrt((points[j][0] - points[i][0])**2 + (points[j][1] - points[i][1])**2 + (points[j][2] - points[i][2])**2)
            if dist < min_distance:
                min_distance = dist
                closest_pair = (points[i], points[j], min_distance)
    
    return closest_pair