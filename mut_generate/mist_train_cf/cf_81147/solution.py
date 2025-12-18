"""
QUESTION:
Write a function `min_distance_pair(points)` that finds the closest pair of points in a given array of points in 2D space, considering the minimum Manhattan distance between the points. The input is a list of tuples, where each tuple represents a point in 2D space. The function should return the pair of points with the minimum Manhattan distance.
"""

def min_distance_pair(points):
    min_distance = float('inf') 
    closest_pair = (None, None) 
    
    n = len(points) 
    for i in range(n):
        for j in range(i+1, n):
            distance = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
            if distance < min_distance:
                min_distance = distance
                closest_pair = (points[i], points[j])
                
    return closest_pair