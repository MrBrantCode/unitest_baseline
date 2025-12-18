"""
QUESTION:
Write a function named `centroid_of_triangle` that calculates the centroid of a triangle given its vertices. The function should take a list of three tuples representing the coordinates (x, y) of the vertices as input and return a tuple representing the coordinates (x, y) of the centroid.
"""

def centroid_of_triangle(vertices):
    x_coords = [point[0] for point in vertices]
    y_coords = [point[1] for point in vertices]
    centroid_x = sum(x_coords) / 3
    centroid_y = sum(y_coords) / 3
    return centroid_x, centroid_y