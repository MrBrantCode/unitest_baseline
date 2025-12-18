"""
QUESTION:
Implement a function `process_coordinates(xy)` that takes a list of coordinates `xy` where each coordinate is either a tuple of two integers or a complex number. Calculate the distance between consecutive Cartesian coordinates and store them in a list, and calculate the magnitude of each complex number and store them in a separate list. Return the two lists. The distance is calculated using the Euclidean distance formula between two points (x1, y1) and (x2, y2) as sqrt((x2-x1)^2 + (y2-y1)^2). The magnitude of a complex number z = a + bj is calculated as sqrt(a^2 + b^2).
"""

import numpy
import math

def process_coordinates(xy):
    distances = []
    magnitudes = []
    last_cartesian_coord = None

    for coord in xy:
        if isinstance(coord, tuple) and len(coord) == 2 and all(isinstance(val, int) for val in coord):
            if last_cartesian_coord is not None:
                distance = math.sqrt((coord[0] - last_cartesian_coord[0])**2 + (coord[1] - last_cartesian_coord[1])**2)
                distances.append(distance)
            last_cartesian_coord = coord
        elif isinstance(coord, complex):
            magnitude = abs(coord)
            magnitudes.append(magnitude)

    return distances, magnitudes