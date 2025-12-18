"""
QUESTION:
Write a function named `find_closest_point` that takes a list of 2D points as input and returns the index of the point that lies closest to the origin [0, 0]. If there are multiple points with the same closest distance, any one of them can be returned.
"""

def find_closest_point(points):
    distances = []
    for point in points:
        distance = (point[0] ** 2 + point[1] ** 2) ** 0.5
        distances.append(distance)
    
    min_distance = min(distances)
    return distances.index(min_distance)