"""
QUESTION:
Implement the `improve_depth` function to improve the quality of a depth map based on a corresponding grayscale image. The function should take three parameters: `gray_img`, a 2D array representing the grayscale image; `original_depth`, a 2D array representing the original depth map; and `threshold`, a float representing the threshold value for depth map improvement. The function should return a 2D array representing the smoothed depth map.
"""

import numpy as np

def improve_depth(gray_img, original_depth, threshold):
    smoothed_depth = np.where(gray_img < threshold, original_depth, original_depth * 1.5)
    return smoothed_depth