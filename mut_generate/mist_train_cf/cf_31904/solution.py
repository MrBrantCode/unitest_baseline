"""
QUESTION:
Implement a function `calculate_weighted_distances` that takes in the coordinates of a reference point `(x1, y1)`, the weights `px` and `py`, the divisor `dd`, and a list of points `points`. The function should return a list of weighted distances between each point in the list and the reference point `(x1, y1)` using the formula `((x2 - x1) * px + (y2 - y1) * py) / max(1e-9, float(dd))`.
"""

from typing import List

def calculate_weighted_distances(x1, y1, px, py, dd, points) -> List[float]:
    weighted_distances = []
    for point in points:
        x2, y2 = point
        distance = ((x2 - x1) * px + (y2 - y1) * py) / max(1e-9, float(dd))
        weighted_distances.append(distance)
    return weighted_distances