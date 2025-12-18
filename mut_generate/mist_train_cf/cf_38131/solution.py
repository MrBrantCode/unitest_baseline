"""
QUESTION:
Implement the `non_max_suppression` function to perform non-maximum suppression (NMS) on a set of bounding boxes based on their confidence scores. The function takes three inputs: `bounding_boxes`, `confidence_scores`, and `threshold`. It returns the indices of the selected bounding boxes after suppression.

Inputs:
- `bounding_boxes`: A list of tuples representing the bounding boxes in the format `(x_min, y_min, x_max, y_max)`, where `(x_min, y_min)` and `(x_max, y_max)` are the coordinates of the top-left and bottom-right corners of the bounding box, respectively.
- `confidence_scores`: A list of confidence scores corresponding to each bounding box.
- `threshold`: The threshold value for suppressing overlapping bounding boxes, ranging from 0 to 1.

Output:
- A list of indices representing the selected bounding boxes after NMS.
"""

from typing import List, Tuple

def non_max_suppression(bounding_boxes: List[Tuple[int, int, int, int]], 
                        confidence_scores: List[float], 
                        threshold: float) -> List[int]:
    """
    Perform non-maximum suppression (NMS) on a set of bounding boxes based on their confidence scores.

    Args:
    - bounding_boxes: A list of tuples representing the bounding boxes in the format (x_min, y_min, x_max, y_max).
    - confidence_scores: A list of confidence scores corresponding to each bounding box.
    - threshold: The threshold value for suppressing overlapping bounding boxes, ranging from 0 to 1.

    Returns:
    - A list of indices representing the selected bounding boxes after NMS.
    """
    def calculate_iou(box1: Tuple[int, int, int, int], box2: Tuple[int, int, int, int]) -> float:
        # Calculate the intersection over union (IoU) of two bounding boxes
        x1 = max(box1[0], box2[0])
        y1 = max(box1[1], box2[1])
        x2 = min(box1[2], box2[2])
        y2 = min(box1[3], box2[3])

        intersection = max(0, x2 - x1) * max(0, y2 - y1)
        area_box1 = (box1[2] - box1[0]) * (box1[3] - box1[1])
        area_box2 = (box2[2] - box2[0]) * (box2[3] - box2[1])
        union = area_box1 + area_box2 - intersection

        return intersection / union

    selected_indices = []
    sorted_indices = sorted(range(len(confidence_scores)), key=lambda i: confidence_scores[i], reverse=True)

    while len(sorted_indices) > 0:
        current_index = sorted_indices[0]
        selected_indices.append(current_index)

        for i in range(1, len(sorted_indices)):
            if calculate_iou(bounding_boxes[current_index], bounding_boxes[sorted_indices[i]]) > threshold:
                sorted_indices.pop(i)
            else:
                i += 1

        sorted_indices.pop(0)

    return selected_indices