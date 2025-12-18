"""
QUESTION:
Create a function named `image_pooling` that performs max pooling on an input image. The function should take two inputs: a 2D NumPy array representing the input image and an integer `window_size` representing the size of the pooling window. The function should return a 2D NumPy array representing the pooled output, where each element is the maximum value from the corresponding non-overlapping region of the input image. The pooling operation should divide the input image into non-overlapping regions of size `window_size x window_size` and take the maximum value from each region.
"""

import numpy as np

def image_pooling(input_image, window_size):
    input_height, input_width = input_image.shape
    output_height = input_height // window_size
    output_width = input_width // window_size
    pooled_output = np.zeros((output_height, output_width))

    for i in range(output_height):
        for j in range(output_width):
            start_row = i * window_size
            end_row = start_row + window_size
            start_col = j * window_size
            end_col = start_col + window_size
            pooled_output[i, j] = np.max(input_image[start_row:end_row, start_col:end_col])

    return pooled_output