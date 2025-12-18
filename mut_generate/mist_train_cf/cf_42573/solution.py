"""
QUESTION:
Write a function `total_area(rectangles)` that calculates the total area covered by all rectangles in a list. The function takes a list of tuples as input, where each tuple contains four integers representing the x and y coordinates of the bottom-left corner of a rectangle, followed by its width and height. The function should account for any overlapping areas. Assume the input list is non-empty and the dimensions of the rectangles are always positive integers.
"""

from typing import List, Tuple

def total_area(rectangles: List[Tuple[int, int, int, int]]) -> int:
    if not rectangles:
        return 0

    x_coords = set()
    y_coords = set()
    for rect in rectangles:
        x_coords.add(rect[0])
        x_coords.add(rect[0] + rect[2])
        y_coords.add(rect[1])
        y_coords.add(rect[1] + rect[3])

    x_coords = sorted(list(x_coords))
    y_coords = sorted(list(y_coords))

    area = 0
    for i in range(len(x_coords) - 1):
        for j in range(len(y_coords) - 1):
            for rect in rectangles:
                if x_coords[i] >= rect[0] and x_coords[i + 1] <= rect[0] + rect[2] and y_coords[j] >= rect[1] and y_coords[j + 1] <= rect[1] + rect[3]:
                    area += (x_coords[i + 1] - x_coords[i]) * (y_coords[j + 1] - y_coords[j])
                    break

    return area