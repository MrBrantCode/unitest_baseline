"""
QUESTION:
Write a function `find_max_distance_vertex` that takes a string of 3D vertex coordinates in the format "VRTX id x y z" as input and returns the IDs of the two vertices with the maximum Euclidean distance between them. The input string contains multiple lines, each representing a vertex, and the vertex IDs are unique. The function should return a tuple of two vertex IDs.
"""

import math

def calculate_distance(x1, y1, z1, x2, y2, z2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)

def find_max_distance_vertex(input_string):
    vertices = input_string.split('\n')
    max_distance = 0
    max_distance_vertices = ()
    
    for i in range(len(vertices)):
        id1, x1, y1, z1 = map(float, vertices[i].split()[1:])
        for j in range(i+1, len(vertices)):
            id2, x2, y2, z2 = map(float, vertices[j].split()[1:])
            distance = calculate_distance(x1, y1, z1, x2, y2, z2)
            if distance > max_distance:
                max_distance = distance
                max_distance_vertices = (int(id1), int(id2))
    
    return max_distance_vertices