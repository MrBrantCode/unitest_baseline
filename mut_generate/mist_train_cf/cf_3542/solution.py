"""
QUESTION:
Implement a function `calculate_shortest_distance(point1, point2, obstacles)` that calculates the shortest distance between two points `point1` and `point2` in a three-dimensional space, considering that there are obstacles present in the environment that the line connecting the points must avoid. Each obstacle is represented by its coordinates and has a certain height, and the line connecting the points must not intersect with any of the obstacles' surfaces. Return the shortest distance as a float value.

The function takes three parameters:
- `point1` and `point2`: tuples representing the coordinates of the two points in 3D space.
- `obstacles`: a list of tuples representing the coordinates of the obstacles.

The function should return the shortest distance between `point1` and `point2` while avoiding the obstacles. If there are no obstacles, the function should return the Euclidean distance between the two points.
"""

def entance(point1, point2, obstacles):
    shortest_distance = None
    for obstacle in obstacles:
        if point1[2] > obstacle[2] and point2[2] > obstacle[2]:
            continue  # Skip this obstacle as line does not intersect with the surface
        distance = ((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2 + (point1[2] - point2[2]) ** 2) ** 0.5
        if shortest_distance is None or distance < shortest_distance:
            shortest_distance = distance
    if shortest_distance is None:
        return ((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2 + (point1[2] - point2[2]) ** 2) ** 0.5
    return shortest_distance