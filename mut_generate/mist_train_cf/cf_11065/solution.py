"""
QUESTION:
Write a function `rectangles_intersect(rect1, rect2)` that determines if two rectangles intersect. Each rectangle is represented by a tuple of four values: the x and y coordinates of its bottom-left corner, and its width and height. The function should return `True` if the rectangles intersect and `False` otherwise. Note that the coordinates of the rectangles can be negative, and the width and height can be zero or negative.
"""

def rectangles_intersect(rect1, rect2):
    x1, y1, w1, h1 = rect1
    x2, y2, w2, h2 = rect2

    return not (x1 > x2 + w2 or x2 > x1 + w1 or y1 > y2 + h2 or y2 > y1 + h1)