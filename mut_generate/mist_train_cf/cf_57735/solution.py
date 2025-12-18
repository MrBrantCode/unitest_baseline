"""
QUESTION:
Write a function named `weighted_std_dev` that calculates the weighted standard deviation of a given column in a pandas DataFrame using another column as weights. The function should exclude outliers in the weights column using the z-score method (considering any data point with a z-score greater than 3 or less than -3 as an outlier). The weights should be normalized to sum up to 1. The function should return the weighted standard deviation.

Note: Do not use any built-in weighted standard deviation method.
"""

import numpy as np

def weighted_std_dev(df, column, weights_column):
    """
    Calculate the weighted standard deviation of a given column in a pandas DataFrame.

    Parameters:
    df (pandas DataFrame): DataFrame containing the data.
    column (str): Name of the column for which the weighted standard deviation is to be calculated.
    weights_column (str): Name of the column to be used as weights.

    Returns:
    float: Weighted standard deviation.
    """

    # Remove outliers using Z-score
    z_scores = np.abs((df[weights_column] - df[weights_column].mean()) / df[weights_column].std())
    df = df[z_scores <= 3]

    # Calculate the weights by normalizing the weights column to sum up to 1
    weights = df[weights_column] / df[weights_column].sum()

    # Calculate the weighted mean
    mean = (df[column] * weights).sum() / weights.sum()

    # Calculate the weighted variance
    variance = ((df[column] - mean) ** 2 * weights).sum() / weights.sum()

    # Standard deviation is the square root of variance
    std_dev = np.sqrt(variance)

    return std_dev