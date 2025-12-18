"""
QUESTION:
Write a function `can_add_rectangle` that takes a 2D grid `canvas` and the top-left and bottom-right coordinates `(x1, y1, x2, y2)` of a new rectangle, and determines if the new rectangle can be added to the canvas without overlapping any existing ones. The canvas is represented as a 2D grid where 1 represents an occupied cell and 0 represents an empty cell. If the new rectangle can be added, the function should update the canvas state and return True; otherwise, it should return False.

The function should take in the following parameters:
- `canvas`: A 2D list of integers representing the current state of the canvas.
- `x1`: The x-coordinate of the top-left corner of the new rectangle.
- `y1`: The y-coordinate of the top-left corner of the new rectangle.
- `x2`: The x-coordinate of the bottom-right corner of the new rectangle.
- `y2`: The y-coordinate of the bottom-right corner of the new rectangle.

The function should return a boolean value indicating whether the new rectangle can be added to the canvas without overlapping any existing ones.
"""

from typing import List

def can_add_rectangle(canvas: List[List[int]], x1: int, y1: int, x2: int, y2: int) -> bool:
    for i in range(x1, x2):
        for j in range(y1, y2):
            if canvas[j][i] == 1:
                return False
    for i in range(x1, x2):
        for j in range(y1, y2):
            canvas[j][i] = 1
    return True