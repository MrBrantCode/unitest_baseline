"""
QUESTION:
Write a function `pareto_mean` that calculates the mean of the Pareto distribution with shape parameter α and scale parameter xm. The function should take α and xm as input parameters and return the mean. If the mean is undefined (i.e., when α is less than or equal to 1), the function should return a message indicating that the mean is undefined.
"""

import math

def pareto_mean(alpha, xm):
    """
    Calculate the mean of the Pareto distribution.

    Args:
    alpha (float): Shape parameter of the Pareto distribution.
    xm (float): Scale parameter of the Pareto distribution.

    Returns:
    float: The mean of the Pareto distribution if alpha > 1, otherwise a message indicating that the mean is undefined.
    """
    if alpha <= 1:
        return "The mean is undefined."
    else:
        return alpha * xm / (alpha - 1)