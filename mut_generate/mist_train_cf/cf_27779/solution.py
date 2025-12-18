"""
QUESTION:
Implement the function `calculate_average_rgb(image_array)` that takes a 3D NumPy array `image_array` representing an image with shape (height, width, 3), where the last dimension represents the RGB channels, and returns a tuple `(avg_red, avg_green, avg_blue)` containing the average RGB values of the entire image.
"""

import numpy as np

def calculate_average_rgb(image_array):
    avg_red = np.mean(image_array[:,:,0])
    avg_green = np.mean(image_array[:,:,1])
    avg_blue = np.mean(image_array[:,:,2])
    return (avg_red, avg_green, avg_blue)