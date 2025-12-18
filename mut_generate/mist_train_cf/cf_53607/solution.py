"""
QUESTION:
Calculate the 95% confidence interval for precision and recall metrics using the Gaussian distribution approximation.

Write a function named `calculate_confidence_interval` that takes in the metric (either precision or recall), the total number of instances (n), and the desired z-score (z) as inputs and returns the radius of the confidence interval. The total number of instances (n) should be interpreted based on the given metric: for precision, n is the total number of positive predictions, and for recall, n is the total number of actual positives. The function should use the formula `radius = z * sqrt( (metric * (1 - metric)) / n)`.
"""

import math

def calculate_confidence_interval(metric, n, z):
    """
    Calculate the radius of the confidence interval for precision and recall metrics.

    Args:
    - metric (float): The precision or recall metric value.
    - n (int): The total number of instances (positive predictions for precision, actual positives for recall).
    - z (float): The desired z-score.

    Returns:
    - float: The radius of the confidence interval.
    """
    radius = z * math.sqrt((metric * (1 - metric)) / n)
    return radius