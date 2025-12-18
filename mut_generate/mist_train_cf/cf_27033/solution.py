"""
QUESTION:
Implement a function named `non_maximum_suppression` that performs non-maximum suppression on a set of detected objects in an image. The function should take three parameters: a list of bounding boxes (`bounding_boxes`), a list of their associated confidence scores (`confidence_scores`), and an overlap threshold (`overlap_threshold`). The function should return a list of filtered bounding boxes after applying non-maximum suppression. The bounding boxes should be represented as tuples of four values (x1, y1, x2, y2) representing the coordinates of the top-left and bottom-right corners. The overlap threshold is a float value between 0 and 1, representing the maximum allowed overlap ratio between two bounding boxes.
"""

def non_maximum_suppression(bounding_boxes, confidence_scores, overlap_threshold):
    def calculate_overlap(box1, box2):
        intersection = max(0, min(box1[2], box2[2]) - max(box1[0], box2[0])) * max(0, min(box1[3], box2[3]) - max(box1[1], box2[1]))
        area1 = (box1[2] - box1[0]) * (box1[3] - box1[1])
        area2 = (box2[2] - box2[0]) * (box2[3] - box2[1])
        union = area1 + area2 - intersection
        overlap = intersection / union
        return overlap

    boxes_with_scores = [(box, score) for box, score in zip(bounding_boxes, confidence_scores)]
    sorted_boxes = sorted(boxes_with_scores, key=lambda x: x[1], reverse=True)
    
    selected_boxes = []
    
    for box, score in sorted_boxes:
        overlaps = [calculate_overlap(box, sel_box) for sel_box in selected_boxes]
        if not any(overlap > overlap_threshold for overlap in overlaps):
            selected_boxes.append(box)
    
    return selected_boxes