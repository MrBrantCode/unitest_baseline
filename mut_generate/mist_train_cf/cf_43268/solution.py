"""
QUESTION:
Write a function `process_people_paths(image_coords_paths, world_coords_paths)` that takes two lists of strings, `image_coords_paths` and `world_coords_paths`, as input and returns a list of strings where each element is a processed path created by combining the corresponding elements from the input lists. The function should process the paths for each person by concatenating the image and world paths with "Processed_" prefix. The length of the output list should be equal to the length of the input lists, which are assumed to be of the same length.
"""

from typing import List

def process_people_paths(image_coords_paths: List[str], world_coords_paths: List[str]) -> List[str]:
    return [f"Processed_{i}_{w}" for i, w in zip(image_coords_paths, world_coords_paths)]