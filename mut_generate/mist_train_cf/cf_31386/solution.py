"""
QUESTION:
Implement a function `imresize(frame_large, target_size)` that resizes an input image `frame_large` to a specified dimension `target_size` using bilinear interpolation. The input image is a NumPy array with shape (height, width, channels), where channels represent the color channels (e.g., RGB). The target dimensions are specified as a tuple (target_height, target_width). The function should return the resized image.
"""

import numpy as np

def imresize(frame_large, target_size):
    target_height, target_width = target_size
    height, width, channels = frame_large.shape

    height_ratio = height / target_height
    width_ratio = width / target_width

    new_height = np.arange(target_height) * height_ratio
    new_width = np.arange(target_width) * width_ratio

    new_x, new_y = np.meshgrid(new_width, new_height)

    old_x = (new_x / width_ratio).astype(int)
    old_y = (new_y / height_ratio).astype(int)

    old_x = np.clip(old_x, 0, width - 1)
    old_y = np.clip(old_y, 0, height - 1)

    top_left = frame_large[old_y, old_x]
    top_right = frame_large[old_y, np.clip(old_x + 1, 0, width - 1)]
    bottom_left = frame_large[np.clip(old_y + 1, 0, height - 1), old_x]
    bottom_right = frame_large[np.clip(old_y + 1, 0, height - 1), np.clip(old_x + 1, 0, width - 1)]

    dx = new_x - old_x
    dy = new_y - old_y
    w1 = (1 - dx) * (1 - dy)
    w2 = dx * (1 - dy)
    w3 = (1 - dx) * dy
    w4 = dx * dy

    resized_frame = w1[:, :, None] * top_left + w2[:, :, None] * top_right + w3[:, :, None] * bottom_left + w4[:, :, None] * bottom_right

    return resized_frame