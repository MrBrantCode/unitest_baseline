"""
QUESTION:
Write a function `rectangles_intersect(rect1, rect2)` that determines if two rectangles intersect. The rectangles are represented by their bottom-left coordinate, width, and height. The coordinates and dimensions of the rectangles can be negative. The function should return True if the rectangles intersect and False otherwise. The rectangles are axis-aligned, meaning their sides are parallel to the x and y axes.
"""

def rectangles_intersect(rect1, rect2):
    # Check if the rectangles intersect by comparing the x and y coordinates
    if rect1[0] > rect2[0] + rect2[2] or rect1[0] + rect1[2] < rect2[0]:
        return False
    if rect1[1] > rect2[1] + rect2[3] or rect1[1] + rect1[3] < rect2[1]:
        return False
    return True