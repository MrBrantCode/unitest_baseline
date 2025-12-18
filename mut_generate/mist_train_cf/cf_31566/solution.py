"""
QUESTION:
Write a Python function `calculate_average_distance(distances)` that takes in a list of distances as floating-point numbers and returns the average distance of the middle 10 readings. The input list must contain at least 10 elements. If the list length is odd, the middle 10 readings will be centered around the middle element. The function should handle cases where the list has more than 10 elements.
"""

from typing import List

def calculate_average_distance(distances: List[float]) -> float:
    center_index = len(distances) // 2
    mid_10_distances = distances[center_index - 5: center_index + 5]
    average_distance = sum(mid_10_distances) / len(mid_10_distances)
    return average_distance