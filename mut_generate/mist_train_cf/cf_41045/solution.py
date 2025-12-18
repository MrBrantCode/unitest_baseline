"""
QUESTION:
Implement the `average_in_region` function to calculate the average value of the elements within a specified rectangular region in a 2D array. The function should take in a 2D array `arr` and the coordinates of the rectangular region defined by `top_left` and `bottom_right`, which are inclusive. The function should return the average value of the elements within the region.

The input `arr` is a 2D array, and `top_left` and `bottom_right` are tuples representing the coordinates of the rectangular region. The coordinates are 0-indexed and inclusive.
"""

import numpy as np

def average_in_region(arr, top_left, bottom_right):
    region = arr[top_left[0]:bottom_right[0]+1, top_left[1]:bottom_right[1]+1]
    return np.mean(region)