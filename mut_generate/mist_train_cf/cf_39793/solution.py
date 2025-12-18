"""
QUESTION:
Given a list of integers representing bottle volumes, write a function `calculate_total_volume` that calculates the total volume of liquid in the bottles, considering that labels may not be in ascending order and some may be missing. The function should take an array of integers `labels` and return the total volume as an integer.

Function signature: `def calculate_total_volume(labels: List[int]) -> int`
"""

from typing import List

def calculate_total_volume(labels: List[int]) -> int:
    if not labels:
        return 0

    max_label = max(labels)
    total_volume = 0
    volumes = [0] * (max_label + 1)

    for label in labels:
        volumes[label] += label

    return sum(volumes)