"""
QUESTION:
Implement a function `calculate_h(keypoint_coords, x0, y0, y_diff)` that takes a 3D array `keypoint_coords` and three integers `x0`, `y0`, `y_diff` as input, where `keypoint_coords` contains the coordinates of keypoints. The function should return a list `h` where each pair of elements are calculated as `(keypoint_coords[0, i, :][1] - x0) / y_diff` and `(-keypoint_coords[0, i, :][0] + y0) / y_diff` for each keypoint `i`.
"""

def entrance(keypoint_coords, x0, y0, y_diff):
    h = []
    for i in range(keypoint_coords.shape[1]):
        h.append((keypoint_coords[0, i, :][1] - x0) / y_diff)
        h.append((-keypoint_coords[0, i, :][0] + y0) / y_diff)
    return h