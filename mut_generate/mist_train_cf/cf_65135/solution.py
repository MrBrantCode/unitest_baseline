"""
QUESTION:
Write a function `trend_similarity` that measures the trend similarity between two curves or time series, excluding the magnitude of movements but considering the direction and timing of rising and falling points and turning points. The function should take two lists of numbers `x` and `y` as input, each representing a curve or time series. The output should be a numerical value representing the trend similarity between the two curves.
"""

import numpy as np

def trend_similarity(x, y):
    """
    Measures the trend similarity between two curves or time series.

    Args:
        x (list): The first curve or time series.
        y (list): The second curve or time series.

    Returns:
        float: A numerical value representing the trend similarity between the two curves.
    """
    # Calculate the correlation between the two curves
    return np.corrcoef(x, y)[0, 1]