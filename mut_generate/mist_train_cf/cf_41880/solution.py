"""
QUESTION:
Write a function `MRF_denoise` that takes an input image `I` and parameters `eta` and `zeta`, and returns the denoised image `J` using the Markov Random Field (MRF) method. The MRF method should consider the relationships between neighboring pixels and use the parameters `eta` and `zeta` to influence the denoising process. The function should return the denoised image after performing multiple iterations of the MRF algorithm. Assume the input image `I` is a 2D numpy array and the parameters `eta` and `zeta` are floating-point numbers.
"""

import numpy as np

def MRF_denoise(I, eta=2.0, zeta=1.5):
    rows, cols = I.shape
    J = np.copy(I)  # Initialize denoised image with the input image

    # Define the neighborhood structure (e.g., 4 or 8 connectivity)
    neighborhood = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # 4-connectivity

    # Perform multiple iterations for denoising
    for _ in range(10):  # Example: 10 iterations
        for i in range(rows):
            for j in range(cols):
                # Calculate energy function for the current pixel
                energy = 0
                for dx, dy in neighborhood:
                    if 0 <= i + dx < rows and 0 <= j + dy < cols:
                        energy += eta * (I[i, j] - I[i + dx, j + dy])**2
                energy += zeta * I[i, j]

                # Update the denoised image based on the energy function
                J[i, j] = np.argmin([energy, 0])  # Example: argmin as a simple threshold

    return J