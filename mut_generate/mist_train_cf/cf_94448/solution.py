"""
QUESTION:
Write a function `find_closest_point(points)` that takes a list of points as input, where each point is a list of two integers representing the x and y coordinates. The function should return the index of the point that lies closest to the origin [0, 0]. If there are multiple points with the same closest distance, the function should return the index of the point with the lowest x-coordinate. If there are still multiple points with the same closest distance and the same x-coordinate, the function should return the index of the point with the lowest y-coordinate.
"""

def entrance(points):
    distances = []
    for point in points:
        distance = (point[0] ** 2 + point[1] ** 2) ** 0.5
        distances.append(distance)
    
    min_distance = min(distances)
    closest_points = [i for i, distance in enumerate(distances) if distance == min_distance]
    closest_points.sort(key=lambda x: (points[x][0], points[x][1]))
    return closest_points[0]