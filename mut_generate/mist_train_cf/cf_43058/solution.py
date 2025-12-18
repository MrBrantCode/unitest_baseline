"""
QUESTION:
Calculate the weighted sum of the largest bounding box based on its width. 

Write a function `calculate_weighted_sum` that takes in three parameters: `stars`, a list of tuples representing the bounding boxes of detected objects where each tuple contains four integers (x, y, w, h); `levelWeights`, a list of integers representing the weights of the detected objects; and `sf`, a float representing a scaling factor. The function should return the weighted sum of the largest bounding box, calculated by multiplying the weight of the largest bounding box by the scaling factor `sf` and the width of the largest bounding box.
"""

from typing import List, Tuple

def calculate_weighted_sum(stars: List[Tuple[int, int, int, int]], levelWeights: List[int], sf: float) -> float:
    if not stars:
        return 0

    max_width_index = max(range(len(stars)), key=lambda i: stars[i][2])
    return float(levelWeights[max_width_index]) * float(sf) * float(stars[max_width_index][2])