"""
QUESTION:
Implement a function `equirectangular_kernel(shape, kernel_size, dilation)` that calculates the kernel differentials for the equirectangular projection. The function should take three parameters: `shape` as a tuple `(height, width)` representing the shape of the input image, `kernel_size` as an integer representing the size of the kernel for the differentials, and `dilation` as an integer representing the dilation factor for the kernel. The function should return two arrays `dlon` and `dlat`, representing the differentials in the longitudinal and latitudinal directions, respectively.
"""

import numpy as np

def entrance(shape, kernel_size, dilation):
    height, width = shape
    dlon = np.zeros((height, width))
    dlat = np.zeros((height, width))

    for i in range(height):
        for j in range(width):
            dlon[i, j] = (j - width // 2) / (width * dilation)
            dlat[i, j] = (i - height // 2) / (height * dilation)

    return dlon, dlat