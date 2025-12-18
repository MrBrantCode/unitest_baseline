"""
QUESTION:
Write a function `calculate_similarity_matrix(input_scores, input_bboxes, keep_top_k)` that takes in the input scores, input bounding boxes, and the keep_top_k value, and returns the similarity matrix based on the IoU metric.

The input_scores is an array representing the confidence scores of detected objects, input_bboxes is an array representing the bounding boxes of detected objects, and keep_top_k is the maximum number of top-scoring bounding boxes to keep. The function should calculate the IoU similarity matrix for the top-k bounding boxes. The IoU metric is defined as the intersection area divided by the union area of two bounding boxes. The bounding box coordinates are represented as [x1, y1, x2, y2] where (x1, y1) is the top-left corner and (x2, y2) is the bottom-right corner.
"""

import numpy as np

def calculate_similarity_matrix(input_scores, input_bboxes, keep_top_k):
    if len(input_bboxes) > keep_top_k:
        indices = np.argsort(-input_scores)[:keep_top_k]
        scores = input_scores[indices]
        bboxes = input_bboxes[indices]
    else:
        scores = np.copy(input_scores)
        indices = np.arange(len(scores))
        bboxes = input_bboxes

    def calculate_iou(box1, box2):
        x1 = max(box1[0], box2[0])
        y1 = max(box1[1], box2[1])
        x2 = min(box1[2], box2[2])
        y2 = min(box1[3], box2[3])

        intersection = max(0, x2 - x1) * max(0, y2 - y1)
        area1 = (box1[2] - box1[0]) * (box1[3] - box1[1])
        area2 = (box2[2] - box2[0]) * (box2[3] - box2[1])
        union = area1 + area2 - intersection

        return intersection / union

    similarity_matrix = np.zeros((len(bboxes), len(bboxes)))
    for i in range(len(bboxes)):
        for j in range(len(bboxes)):
            similarity_matrix[i, j] = calculate_iou(bboxes[i], bboxes[j])

    return similarity_matrix