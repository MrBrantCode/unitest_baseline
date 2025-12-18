"""
QUESTION:
Write a function `check_rectangle_overlap(rect1, rect2)` that checks if two rectangles overlap with each other. The rectangles are represented by their top-left and bottom-right coordinates in tuples `rect1` and `rect2`. The function should return a boolean value indicating whether the two rectangles overlap or not. The coordinates can be negative.
"""

def entrance(rect1, rect2):
    x1, y1, x2, y2 = rect1
    x3, y3, x4, y4 = rect2

    if x1 > x4 or x2 < x3:
        return False

    if y1 > y4 or y2 < y3:
        return False

    return True