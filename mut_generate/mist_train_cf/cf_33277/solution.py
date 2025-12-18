"""
QUESTION:
Write a function `calculate_distances(lines)` that takes in a list of strings representing pairs of coordinates in the format "x1,y1 -> x2,y2". Calculate the Euclidean distance between each pair of coordinates and return the distances as a list of floating-point numbers rounded to two decimal places. Assume the input coordinates are valid. The distance between two points (x1, y1) and (x2, y2) is calculated using the formula: distance = sqrt((x2 - x1)^2 + (y2 - y1)^2).
"""

from typing import List
import math

def calculate_distances(lines: List[str]) -> List[float]:
    distances = []
    for line in lines:
        coordinates = line.split(' -> ')
        x1, y1 = map(int, coordinates[0].split(','))
        x2, y2 = map(int, coordinates[1].split(','))
        distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
        distances.append(round(distance, 2))
    return distances