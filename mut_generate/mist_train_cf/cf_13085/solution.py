"""
QUESTION:
Create a function named `classify_coordinates` that classifies a given set of 2D coordinates into four categories based on the signs of their X and Y values: 
1. Positive X and Positive Y
2. Positive X and Negative Y
3. Negative X and Positive Y
4. Negative X and Negative Y

The function should also identify and classify outliers, which are defined as coordinates with absolute values greater than a given threshold (e.g., 5). The function should return the classification result as a string.
"""

import numpy as np

def classify_coordinates(coord, outlier_threshold=5):
    """
    Classify a given set of 2D coordinates into four categories based on the signs of their X and Y values.
    Also identify and classify outliers, which are defined as coordinates with absolute values greater than a given threshold.

    Args:
        coord (list or numpy array): A list or numpy array of two elements representing the X and Y coordinates.
        outlier_threshold (int, optional): The threshold value for identifying outliers. Defaults to 5.

    Returns:
        str: The classification result of the given coordinates.
    """

    # Check for outliers
    if np.abs(coord[0]) > outlier_threshold or np.abs(coord[1]) > outlier_threshold:
        return "Outlier"
    
    # Classify the coordinates based on signs
    if coord[0] >= 0 and coord[1] >= 0:
        return "Positive X and Positive Y"
    elif coord[0] >= 0 and coord[1] < 0:
        return "Positive X and Negative Y"
    elif coord[0] < 0 and coord[1] >= 0:
        return "Negative X and Positive Y"
    else:
        return "Negative X and Negative Y"