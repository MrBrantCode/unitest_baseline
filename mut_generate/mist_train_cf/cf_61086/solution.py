"""
QUESTION:
Write a function `calculate_distances` that calculates the Euclidean distance between an origin point and each point in a list of point coordinates. The function should handle and correct erroneous points by ignoring non-integer values or invalid inputs. The origin point and point coordinates are represented as tuples of two integers.
"""

import math

def calculate_distances(origin, points):
    distances = []
    for point in points:
        try:
            x_dist = int(point[0]) - origin[0]
            y_dist = int(point[1]) - origin[1]
            distance = math.sqrt(x_dist**2 + y_dist**2)
            distances.append(distance)
        except:
            pass
    return distances