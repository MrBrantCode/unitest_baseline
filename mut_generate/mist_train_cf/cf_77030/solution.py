"""
QUESTION:
Given a list of coordinates and an integer k, implement a function `kFarthestPoints(coordinates, k)` that returns the k points in the coordinates list that are farthest from the origin (0, 0). The distance between two points on the X-Y plane is the Euclidean distance. The function should return the k farthest points in any order, as the answer is guaranteed to be unique except for the order. The function should satisfy the constraints: 1 <= k <= coordinates.length <= 10^4 and -10^4 < xi, yi < 10^4.
"""

import heapq

def kFarthestPoints(coordinates, k):
    # Define a function to calculate distance from origin.
    def distance(coord):
        x, y = coord
        return (x * x + y * y) ** 0.5
        
    # Use heapq.nlargest() to get the k coordinates with the largest distances from origin.
    return heapq.nlargest(k, coordinates, key=distance)