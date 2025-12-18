"""
QUESTION:
Write a function `overlap` that takes two rectangles as input, represented by their integer coordinates (x1, y1, x2, y2), where (x1, y1) is the top-left point and (x2, y2) is the bottom-right point. The function should return the area of the overlapped region if the rectangles overlap, and a message indicating "No overlap" otherwise. The function should not use any built-in libraries or functions for calculations.
"""

def overlap(rect1, rect2):
    x1, y1, x2, y2 = rect1
    a1, b1, a2, b2 = rect2

    # Calculate the overlap between the rectangles
    x_overlap = max(0, min(x2, a2) - max(x1, a1))
    y_overlap = max(0, min(y2, b2) - max(y1, b1))

    # If both overlaps are positive, the rectangles overlap
    if x_overlap > 0 and y_overlap > 0:
        return x_overlap * y_overlap
    else:
        return "No overlap"