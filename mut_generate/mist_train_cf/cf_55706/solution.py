"""
QUESTION:
Given a dataset of 15,000 samples with ages between 9 and 20 and a mean no smaller than 9, determine what can be concluded about the distribution of the samples if the standard deviation is claimed to be 16. The function should check if the claimed standard deviation is plausible.
"""

import math

def is_standard_deviation_plausible(min_age, max_age, mean_age, standard_deviation, num_samples):
    """
    Checks if the claimed standard deviation is plausible given the age range and mean.

    Args:
    min_age (int): The minimum age in the dataset.
    max_age (int): The maximum age in the dataset.
    mean_age (int): The mean age in the dataset.
    standard_deviation (int): The claimed standard deviation.
    num_samples (int): The number of samples in the dataset.

    Returns:
    bool: True if the standard deviation is plausible, False otherwise.
    """

    # Calculate the maximum possible standard deviation
    max_std_dev = (max_age - min_age) / 2

    # Check if the claimed standard deviation is less than or equal to the maximum possible standard deviation
    return standard_deviation <= max_std_dev

def check_std_dev():
    min_age = 9
    max_age = 20
    mean_age = 14.5  # Assuming a mean age of 14.5 for demonstration purposes
    std_dev = 16
    num_samples = 15000
    if is_standard_deviation_plausible(min_age, max_age, mean_age, std_dev, num_samples):
        return True
    else:
        return False

def entrance():
    return check_std_dev()