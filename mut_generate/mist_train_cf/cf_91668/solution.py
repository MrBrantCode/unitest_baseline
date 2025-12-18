"""
QUESTION:
Write a function `rectangles_intersect` that takes two rectangles, each represented by a tuple of four numbers (x, y, w, h), where (x, y) is the bottom-left coordinate and w and h are the width and height, respectively. The function should return True if the rectangles intersect and False otherwise. The coordinates, width, and height can be negative or zero.
"""

def rectangles_intersect(rect1, rect2):
    x1, y1, w1, h1 = rect1
    x2, y2, w2, h2 = rect2

    # Check if the rectangles do not intersect in any way
    if x1 > x2 + w2 or x2 > x1 + w1 or y1 > y2 + h2 or y2 > y1 + h1:
        return False
    else:
        return True