"""
QUESTION:
Implement a function `calculate_iou(gt, pred)` that calculates the Intersection over Union (IoU) for object detection given the coordinates of the ground truth bounding box (gt) and the predicted bounding box (pred). The input bounding boxes are represented as tuples of four elements (x1, y1, x2, y2) denoting the top-left and bottom-right corners. The function should return the IoU value rounded to 4 decimal places.
"""

def calculate_iou(gt, pred):
    # Calculate the coordinates of the intersection rectangle
    x1 = max(gt[0], pred[0])
    y1 = max(gt[1], pred[1])
    x2 = min(gt[2], pred[2])
    y2 = min(gt[3], pred[3])

    # Calculate the area of intersection
    intersection_area = max(0, x2 - x1 + 1) * max(0, y2 - y1 + 1)

    # Calculate the area of the ground truth and predicted bounding boxes
    gt_area = (gt[2] - gt[0] + 1) * (gt[3] - gt[1] + 1)
    pred_area = (pred[2] - pred[0] + 1) * (pred[3] - pred[1] + 1)

    # Calculate the area of union
    union_area = gt_area + pred_area - intersection_area

    # Calculate the IoU
    iou = intersection_area / union_area

    return round(iou, 4)