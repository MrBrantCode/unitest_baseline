"""
QUESTION:
Write a function `calculate_polygon_area` that calculates the areas of given polygons using the shoelace formula. The function takes a list of polygons as input, where each polygon is represented as a list of vertices with x and y coordinates. The function returns a list of the respective areas of the polygons. The input is a list of lists of lists of floats, and the output is a list of floats.
"""

from typing import List

def calculate_polygon_area(polygons: List[List[List[float]]]) -> List[float]:
    areas = []
    for polygon in polygons:
        n = len(polygon)
        area = 0.0
        for i in range(n):
            j = (i + 1) % n
            area += polygon[i][0] * polygon[j][1]
            area -= polygon[j][0] * polygon[i][1]
        area = abs(area) / 2.0
        areas.append(area)
    return areas