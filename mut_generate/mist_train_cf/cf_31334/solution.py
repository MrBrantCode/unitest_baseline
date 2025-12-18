"""
QUESTION:
You are given a list of points on the X-Y plane and an integer k. Write a function `kClosest(points, k)` that returns the k closest points to the origin (0, 0) using the Euclidean distance formula. The function should take in a list of points `points` where each point is a list of two integers and an integer `k`, and return a list of the k closest points in any order.
"""

from typing import List

def kClosest(points: List[List[int]], k: int) -> List[List[int]]:
    # Calculate the distance of each point from the origin using the Euclidean distance formula
    distances = [(point, point[0]**2 + point[1]**2) for point in points]
    
    # Sort the points based on their distances from the origin
    distances.sort(key=lambda x: x[1])
    
    # Return the first k points from the sorted list
    return [point[0] for point in distances[:k]]