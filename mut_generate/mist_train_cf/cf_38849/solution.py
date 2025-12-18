"""
QUESTION:
Write a function `draw_text_rectangles` that takes in six parameters: `n_boxes`, `text`, `left`, `top`, `width`, and `height`, and returns the coordinates of rectangles to be drawn around non-empty text regions within bounding boxes. The input lists `text`, `left`, `top`, `width`, and `height` will all have `n_boxes` elements.

- `n_boxes`: An integer representing the number of bounding boxes.
- `text`: A list of strings representing the text content within each bounding box.
- `left`: A list of integers representing the x-coordinate of the top-left corner of each bounding box.
- `top`: A list of integers representing the y-coordinate of the top-left corner of each bounding box.
- `width`: A list of integers representing the width of each bounding box.
- `height`: A list of integers representing the height of each bounding box.

The function should return a list of tuples, where each tuple contains four integers: x-coordinate of the top-left corner, y-coordinate of the top-left corner, width, and height of the rectangle.
"""

from typing import List, Tuple

def draw_text_rectangles(n_boxes: int, text: List[str], left: List[int], top: List[int], width: List[int], height: List[int]) -> List[Tuple[int, int, int, int]]:
    rectangles = []
    for i in range(n_boxes):
        if text[i].strip() != '':
            x, y, w, h = left[i], top[i], width[i], height[i]
            rectangles.append((x, y, w, h))
    return rectangles