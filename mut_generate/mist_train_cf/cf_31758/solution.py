"""
QUESTION:
Write a function `calculate_areas(rectangles: List[Tuple[str, Tuple[int, int, int, int]]]) -> Dict[str, int]` that takes a list of tuples as input, where each tuple contains a string and a tuple of four integers representing the coordinates and dimensions of a rectangle. The function should return a dictionary where the keys are the strings and the values are the areas of the corresponding rectangles, calculated as the product of the width and height.
"""

from typing import List, Tuple, Dict

def calculate_areas(rectangles: List[Tuple[str, Tuple[int, int, int, int]]]) -> Dict[str, int]:
    areas = {}
    for code, (x, y, width, height) in rectangles:
        areas[code] = width * height
    return areas