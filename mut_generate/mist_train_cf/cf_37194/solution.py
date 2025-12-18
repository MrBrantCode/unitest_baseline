"""
QUESTION:
Implement a function `calculate_iou` that calculates the Intersection over Union (IoU) for two bounding boxes. The function should take in two pairs of width and height (`wh1` and `wh2`) as input and return the IoU for the given width-height pairs. The IoU is calculated as the ratio of the area of intersection to the area of union of the two bounding boxes.
"""

def calculate_iou(wh1, wh2):
    """
    Calculate the Intersection over Union (IoU) for two bounding boxes.

    Args:
        wh1 (tuple, list): width and height pair for the first box
        wh2 (tuple, list): width and height pair for the second box

    Returns:
        iou (float): intersection/union for the given w-h pairs
    """
    w1, h1 = wh1[0], wh1[1]
    w2, h2 = wh2[0], wh2[1]
    intersect_area = min(w1, w2) * min(h1, h2)
    union_area = w1 * h1 + w2 * h2 - intersect_area
    iou = intersect_area / union_area
    return iou