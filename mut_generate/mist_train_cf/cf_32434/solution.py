"""
QUESTION:
Implement the `adjust_contrast` function to take an input image as a numpy array and a contrast level as a scalar in the range [0, 1]. The function should return the image scaled to the specified contrast level. Ensure the function checks for invalid contrast levels and performs necessary operations to adjust the image's contrast. 

The function signature should be `def adjust_contrast(image, contrast_level)`.
"""

import numpy as np

def adjust_contrast(image, contrast_level):
    """
    Return the image scaled to a certain contrast level in [0, 1].

    Parameters:
    - image: a numpy.ndarray representing the input image
    - contrast_level: a scalar in [0, 1]; with 1 -> full contrast

    Returns:
    - numpy.ndarray: the adjusted image with the specified contrast level
    """

    assert contrast_level >= 0.0, "contrast_level too low."
    assert contrast_level <= 1.0, "contrast_level too high."

    # Ensure the image is in the range [0, 1]
    image = np.clip(image, 0, 1)

    # Adjust contrast using linear transformation
    adjusted_image = (image - 0.5) * contrast_level + 0.5
    adjusted_image = np.clip(adjusted_image, 0, 1)

    return adjusted_image