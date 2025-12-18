"""
QUESTION:
Implement a function `num_model_detection_error(ground_truth_vps, detected_vps)` that calculates the average error in the number of detected vanishing points compared to the ground truth vanishing points. The input `ground_truth_vps` and `detected_vps` are lists of vanishing points, each represented as a tuple of two integers corresponding to its x and y coordinates in the image plane. The error is measured as the average logarithm of the distance between each detected vanishing point and its corresponding ground truth vanishing point. If there are more detected vanishing points than ground truth vanishing points, or vice versa, the excess points are ignored. The function should return the average error.
"""

import math

def num_model_detection_error(ground_truth_vps, detected_vps):
    seen_gt_vps = set()
    seen_dt_vps = set()
    total_error = 0

    for gt_vp, dt_vp in zip(ground_truth_vps, detected_vps):
        distance = math.sqrt((dt_vp[0] - gt_vp[0])**2 + (dt_vp[1] - gt_vp[1])**2)
        if gt_vp in seen_gt_vps or dt_vp in seen_dt_vps:
            continue
        seen_gt_vps.add(gt_vp)
        seen_dt_vps.add(dt_vp)
        if distance > 0:
            total_error += math.log(distance)

    return total_error / min(len(detected_vps), len(ground_truth_vps))