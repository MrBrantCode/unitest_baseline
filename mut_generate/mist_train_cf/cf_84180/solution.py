"""
QUESTION:
Write a function `calculate_areas` that takes a list of triangles as input, where each triangle is represented as a tuple of its base and height. The function should calculate and return the areas of the triangles with non-negative base and height, ignoring any triangles with negative parameters.
"""

def calculate_areas(triangle_list):
    areas = []
    for triangle in triangle_list:
        base, height = triangle
        if base >= 0 and height >= 0:
            area = 0.5 * base * height
            areas.append(area)
    return areas