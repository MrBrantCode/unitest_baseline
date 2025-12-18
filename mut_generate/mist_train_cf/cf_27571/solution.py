"""
QUESTION:
Create a function `calculatePolygonArea` that takes a string `svgData` as input. The `svgData` will be a string representing SVG data with one or more `<polygon>` tags, where each tag has a `points` attribute containing the coordinates of the polygon's vertices. The function should extract the coordinates of all the polygons, calculate the total area of all the polygons combined using the Shoelace formula, and return the total area rounded to two decimal places. Assume the SVG data is well-formed and contains at least one polygon.
"""

import re

def calculatePolygonArea(svgData):
    totalArea = 0
    polygonPattern = r'<polygon points="((\d+,\d+\s?)+)"\/>'
    polygons = re.findall(polygonPattern, svgData)

    for polygon in polygons:
        coordinates = polygon[0].split()
        x = [int(coord.split(',')[0]) for coord in coordinates]
        y = [int(coord.split(',')[1]) for coord in coordinates]

        area = 0.5 * abs(sum(x[i] * y[i + 1] - x[i + 1] * y[i] for i in range(len(x) - 1)) + x[-1] * y[0] - x[0] * y[-1])
        totalArea += area

    return round(totalArea, 2)