"""
QUESTION:
Write a function `overlap(rec1, rec2)` that takes two rectangles `rec1` and `rec2` as input, each represented by a list `[x1, y1, x2, y2]`, where `(x1, y1)` is the bottom-left corner and `(x2, y2)` is the top-right corner. The function should return `True` if the rectangles overlap and `False` otherwise. The rectangles' top and bottom edges are parallel to the X-axis, and their left and right edges are parallel to the Y-axis. Overlap is defined as a positive intersection area, excluding cases where rectangles merely touch at the corner or edges. The constraints are `len(rec1) == len(rec2) == 4`, `-109 <= rec1[i], rec2[i] <= 109`, `rec1[0] <= rec1[2]`, `rec1[1] <= rec1[3]`, `rec2[0] <= rec2[2]`, and `rec2[1] <= rec2[3]`.
"""

def isRectangleOverlap(rec1, rec2):
    if rec1[2] <= rec2[0] or rec2[2] <= rec1[0] or rec1[3] <= rec2[1] or rec2[3] <= rec1[1]:
        return False
    else:
        return True