"""
QUESTION:
How can a Convolutional Neural Network (CNN) be designed to produce output images with pixel values in the range [0,1] without defining additional constraints in the optimization problem?
"""

def produce_normalized_image(x):
    """
    Produces an image with pixel values in the range [0,1] using the sigmoid activation function.

    Args:
        x (numpy array): Input image.

    Returns:
        numpy array: Output image with pixel values in the range [0,1].
    """
    import numpy as np

    # Apply the sigmoid activation function to the input image
    normalized_image = 1 / (1 + np.exp(-x))

    return normalized_image