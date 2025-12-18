"""
QUESTION:
Write a function named `hoeffding_sample_size` to calculate the required number of examples for the IID test set using Hoeffding's inequality. The function should take two parameters: `epsilon` (the acceptable difference between the empirical mean and the expected mean) and `delta` (the maximum probability that the empirical mean differs from the expected mean by at least epsilon). The function should return the minimum number of examples required.
"""

import math

def hoeffding_sample_size(epsilon, delta):
    """
    Calculate the required number of examples for the IID test set using Hoeffding's inequality.

    Args:
        epsilon (float): The acceptable difference between the empirical mean and the expected mean.
        delta (float): The maximum probability that the empirical mean differs from the expected mean by at least epsilon.

    Returns:
        int: The minimum number of examples required.
    """
    return math.ceil(math.log(2/delta) / (2*epsilon**2))