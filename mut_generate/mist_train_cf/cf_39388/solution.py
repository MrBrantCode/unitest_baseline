"""
QUESTION:
Implement a function `calculate_masked_sub_pixel_variance` that takes the following inputs:
- `block_size`: A tuple representing the width and height of the block.
- `mask`: A 2D array of 0s and 1s specifying which pixels to include in the variance calculation.
- `pixels`: A 2D array representing the pixel values within the block.

Calculate the masked sub-pixel variance and return the result as a floating-point number.
"""

import numpy as np

def calculate_masked_sub_pixel_variance(block_size, mask, pixels):
    block_width, block_height = block_size
    mask = np.array(mask)
    pixels = np.array(pixels)

    included_pixels = pixels[mask == 1]  # Select pixels based on the mask
    mean_value = np.mean(included_pixels)  # Calculate the mean of included pixels
    squared_diff = (included_pixels - mean_value) ** 2  # Calculate squared differences
    variance = np.mean(squared_diff)  # Calculate the variance

    return variance