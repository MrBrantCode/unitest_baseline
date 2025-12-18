"""
QUESTION:
Write a function `calculate_final_position` that takes in an offset and returns the final position of a 3D model after applying the offset. The offset is a tuple of three float values representing the x, y, and z offsets, and the initial position of the model is at the origin (0, 0, 0) in a right-handed coordinate system. The function should return a tuple of three float values representing the final position.
"""

from typing import Tuple

def calculate_final_position(offset: Tuple[float, float, float]) -> Tuple[float, float, float]:
    initial_position = (0, 0, 0)
    final_position = (initial_position[0] + offset[0], initial_position[1] + offset[1], initial_position[2] + offset[2])
    return final_position