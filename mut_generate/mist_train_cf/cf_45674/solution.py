"""
QUESTION:
Create a function `batch_normalization_beta` that scales the standardized input by a factor β. The function should not restrict β to be greater than zero.
"""

def batch_normalization_beta(x, beta):
    """
    Scales the standardized input by a factor β.

    Parameters:
    x (array_like): Input array to be scaled.
    beta (float): Scaling factor.

    Returns:
    array_like: Scaled input array.
    """
    return x * beta