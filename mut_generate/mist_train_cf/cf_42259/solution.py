"""
QUESTION:
Write a function `process_point_cloud` that takes a 3D NumPy array `point_cloud` and an integer `num_keypoints` as input, and an optional boolean parameter `normal` defaulting to False. 

The function should return a dictionary `end_points` containing two keys: 'xyz' and 'sampled_points'. The value for 'xyz' should be the entire `point_cloud`, and the value for 'sampled_points' should be the first `num_keypoints` points from the `point_cloud`. 

If `normal` is True, the function should also extract the sub-array consisting of all rows and the columns from index 3 to 5 (inclusive) from the `point_cloud`, although this extracted data does not need to be included in the returned dictionary.
"""

import numpy as np

def process_point_cloud(point_cloud, num_keypoints, normal=False):
    if normal:
        _ = point_cloud[:, 3:6]
    
    return {'xyz': point_cloud, 'sampled_points': point_cloud[:num_keypoints]}