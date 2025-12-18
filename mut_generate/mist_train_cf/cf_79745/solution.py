"""
QUESTION:
Write a function `split_normal_distribution` to split a normal distribution `N(mean, std_dev)` into `n` roughly-equal sized pieces. Assume that `mean` and `std_dev` are positive integers, and `n` is a positive integer greater than 1.
"""

import numpy as np

def split_normal_distribution(mean, std_dev, n):
    """
    Split a normal distribution N(mean, std_dev) into n roughly-equal sized pieces.

    Parameters:
    mean (int): The mean of the normal distribution.
    std_dev (int): The standard deviation of the normal distribution.
    n (int): The number of pieces to split the distribution into.

    Returns:
    tuple: A tuple of n normal distributions, each with a mean of mean/n and a standard deviation of std_dev/sqrt(n).
    """

    # Calculate the mean and standard deviation for each piece
    piece_mean = mean / n
    piece_std_dev = std_dev / np.sqrt(n)

    # Return the split distributions
    return [(piece_mean, piece_std_dev) for _ in range(n)]