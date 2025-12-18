"""
QUESTION:
Implement a function `select_region_by_color(image, color)` that takes in a 3D NumPy array `image` representing an image with height, width, and color channels, and a list `color` of RGB values. The function should return a list of tuples containing the (x, y) coordinates of the pixels in the image that exactly match the specified color.
"""

import numpy

def select_region_by_color(image, color):
    matching_pixels = []
    for y in range(image.shape[0]):
        for x in range(image.shape[1]):
            if numpy.array_equal(image[y, x, :], color):
                matching_pixels.append((x, y))
    return matching_pixels