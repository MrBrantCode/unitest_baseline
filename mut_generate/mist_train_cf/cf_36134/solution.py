"""
QUESTION:
Implement the `coordinate_mapping` function that takes in a scale factor `scale`, a boolean flag `antialiasing`, and the output length `out_length`. The function should calculate the output-space coordinates and the corresponding input-space coordinates based on the provided scale factor and antialiasing flag. If the scale factor is less than 1 and antialiasing is enabled, modify the kernel width for interpolation and antialiasing. The function should return the output-space coordinates `x` and the corresponding input-space coordinates `u`. The kernel width and the length of the input space are not provided.
"""

import numpy as np

def coordinate_mapping(scale, antialiasing, out_length, kernel_width):
    if (scale < 1) and (antialiasing):
        kernel_width = kernel_width / scale

    x = np.linspace(1, out_length, out_length)
    u = x / scale + 0.5 * (1 - 1 / scale)

    return x, u