"""
QUESTION:
Implement the `transform_to_complex` function, which takes an input array of shape (batch_size, N, N, 2) containing real and imaginary parts, and returns a complex-valued array of shape (batch_size, N, N, 1) by combining the real and imaginary parts of the input array to form complex numbers.
"""

import numpy as np

def transform_to_complex(array):
    """
    Transforms the input array into a complex-valued array.

    Args:
    array (ndarray): Input array of shape (batch_size, N, N, 2) containing real and imaginary parts.

    Returns:
    joined_array(complex): A complex-valued array of shape (batch_size, N, N, 1)
    """
    real_part = array[:, :, :, 0]  # Extract the real part from the input array
    imag_part = array[:, :, :, 1]  # Extract the imaginary part from the input array
    joined_array = real_part + 1j * imag_part  # Combine real and imaginary parts to form complex numbers
    return joined_array[:, :, :, np.newaxis]