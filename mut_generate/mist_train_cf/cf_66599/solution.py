"""
QUESTION:
Write a function `calculate_distances` that takes a list of 2D points as input, where each point is represented as a tuple of two integers or floats. The function should calculate the Euclidean distance between each consecutive pair of points in the list and return a list of these distances, rounded to two decimal places.
"""

def calculate_distances(points):
    distances = []
    for i in range(len(points) - 1): 
        p1 = points[i]
        p2 = points[i+1]
        distance = ((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)**0.5
        distance = round(distance, 2) 
        distances.append(distance)
    return distances