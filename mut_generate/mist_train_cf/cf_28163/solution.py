"""
QUESTION:
Write a function `first_quadrant_coordinates` that takes a list of tuples representing 2D coordinates and returns a new list containing only the coordinates where both x and y are positive. The input list has a maximum length of 1000, and each coordinate's x and y values range from -1000 to 1000.
"""

from typing import List, Tuple

def first_quadrant_coordinates(coordinates: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
    first_quadrant = []
    for x, y in coordinates:
        if x > 0 and y > 0:
            first_quadrant.append((x, y))
    return first_quadrant