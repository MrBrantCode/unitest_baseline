"""
QUESTION:
Create a function `countShapes(shapes: List[str]) -> Dict[str, int]` where `shapes` is a list of strings representing the names of 3D shapes. The function should return a dictionary where the keys are the unique shape names and the values are the counts of each shape in the input list.
"""

from typing import List, Dict

def entrance(shapes: List[str]) -> Dict[str, int]:
    shape_counts = {}
    for shape in shapes:
        if shape in shape_counts:
            shape_counts[shape] += 1
        else:
            shape_counts[shape] = 1
    return shape_counts