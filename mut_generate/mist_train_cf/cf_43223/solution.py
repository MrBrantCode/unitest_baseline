"""
QUESTION:
Create a function `calculate_weighted_histogram` that takes in three parameters: `theta`, `weight`, and `theta_bins`. `theta` is a list of angle data, `weight` is a list of corresponding weights calculated based on `theta`, and `theta_bins` is the number of bins for the histogram. The function should calculate a weighted histogram based on `theta` and `weight`. 

Restrictions: The function should first check if the number of elements in `weight` is equal to the number of elements in `theta`. If not, it should print an error message and exit the program. The function should use the `histogram` function to calculate the weighted histogram.
"""

import numpy as np

def calculate_weighted_histogram(theta, weight, theta_bins):
    """
    Calculate a weighted histogram based on theta and weight.

    Parameters:
    theta (list): A list of angle data.
    weight (list): A list of corresponding weights calculated based on theta.
    theta_bins (int): The number of bins for the histogram.

    Returns:
    h (numpy.ndarray): The weighted histogram values.
    theta_edge (numpy.ndarray): The bin edges for the histogram.
    """
    if len(weight) != len(theta):
        print('Error: Number of weights and angle data points are inconsistent!')
        print('ABORT')
        import sys
        sys.exit(2)

    h, theta_edge = np.histogram(theta, weights=weight, bins=theta_bins)
    return h, theta_edge