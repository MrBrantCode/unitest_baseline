"""
QUESTION:
Write a function `average_latitude` that calculates the average of a list of latitude coordinates. The function should take a list of float values representing latitude coordinates in degrees, ranging from -90 to 90, and return the average latitude as a float. If the input list is empty, the function should return 0.0.
"""

from typing import List

def average_latitude(latitudes: List[float]) -> float:
    if not latitudes:
        return 0.0  
    return sum(latitudes) / len(latitudes)