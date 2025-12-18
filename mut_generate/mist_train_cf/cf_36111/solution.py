"""
QUESTION:
Write a function `calculate_intersection_area(bbox, cbox)` that takes two bounding boxes `bbox` and `cbox` as input, each represented as a tuple of four integers (x1, y1, x2, y2), where (x1, y1) represents the top-left corner and (x2, y2) represents the bottom-right corner of the bounding box. The function should return the area of the intersection of the two bounding boxes. If the two bounding boxes do not intersect, the function should return 0.
"""

def calculate_intersection_area(bbox, cbox):
    x1 = max(bbox[0], cbox[0])
    y1 = max(bbox[1], cbox[1])
    x2 = min(bbox[2], cbox[2])
    y2 = min(bbox[3], cbox[3])

    w = max(0, x2 - x1)
    h = max(0, y2 - y1)

    return w * h