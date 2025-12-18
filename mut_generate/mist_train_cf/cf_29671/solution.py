"""
QUESTION:
Write a function `reverse_ink_processing(processed_ink, class_name)` where:
- `processed_ink` is a 2D numpy array representing the processed ink strokes, which was processed by normalizing the size to fit within a specific range and computing the differences between consecutive points.
- `class_name` is a string representing the class name associated with the ink strokes.

The function should return the original ink strokes and class name before the size normalization and delta computation were applied.
"""

import numpy as np

def entance(processed_ink, class_name):
    """
    Reverses the ink processing to obtain the original ink strokes and class name.

    Args:
    processed_ink (numpy.ndarray): A 2D numpy array representing the processed ink strokes.
    class_name (str): A string representing the class name associated with the ink strokes.

    Returns:
    tuple: A tuple containing the original ink strokes and the class name.
    """

    # 1. Reverse Compute deltas.
    original_ink = np.zeros((processed_ink.shape[0] + 1, processed_ink.shape[1]))
    original_ink[0, :] = processed_ink[0, :]
    original_ink[1:, 0:2] = np.cumsum(processed_ink[:, 0:2], axis=0)

    # 2. Reverse Size normalization.
    lower = np.min(original_ink[:, 0:2], axis=0)
    upper = np.max(original_ink[:, 0:2], axis=0)
    scale = upper - lower
    scale[scale == 0] = 1
    original_ink[:, 0:2] = original_ink[:, 0:2] * scale + lower

    return original_ink, class_name