"""
QUESTION:
Write a function named `hoeffding_sample_size` that takes three parameters: the desired maximum deviation from the true value (`epsilon`), the desired confidence level (`confidence`), and returns the minimum required sample size (`n`). The function should use Hoeffding's inequality to calculate `n`, where the confidence level is the probability that the empirical mean is within `epsilon` of the true mean. Assume that the data is independently and identically distributed (IID). The function should return `n` as an integer, rounded up to the nearest whole number.
"""

import math

def hoeffding_sample_size(epsilon, confidence):
    """
    Calculate the minimum required sample size using Hoeffding's inequality.

    Parameters:
    epsilon (float): The desired maximum deviation from the true value.
    confidence (float): The desired confidence level.

    Returns:
    int: The minimum required sample size.
    """
    n = -math.log(1 - confidence / 2) / (2 * epsilon ** 2)
    return math.ceil(n)