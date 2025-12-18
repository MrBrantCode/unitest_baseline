"""
QUESTION:
Write a function named `calculate_statistics` to calculate the average, variance, and standard deviation of each list in a 2D list and the entire list as a whole using numpy. The function should take a 2D list of integers as input, and the 2D list should contain at least one sublist with at least one integer.
"""

import numpy as np

def calculate_statistics(nested_list):
    """
    Calculate the average, variance, and standard deviation of each list in a 2D list and the entire list as a whole.

    Args:
        nested_list (list): A 2D list of integers.

    Returns:
        tuple: A tuple containing the average, variance, and standard deviation of each list and the entire list.
    """

    # Calculate the average
    average = np.mean(nested_list, axis=1)  # This calculates the average for each individual list
    total_average = np.mean(nested_list)  # This calculates the average of all the numbers in the nested list  

    # Calculate the variance
    variance = np.var(nested_list, axis=1)  # This calculates the variance for each individual list
    total_variance = np.var(nested_list)  # This calculates the variance of all the numbers in the nested list

    # Calculate the standard deviation
    std_dev = np.std(nested_list, axis=1)  # This calculates the standard deviation for each individual list
    total_std_dev = np.std(nested_list)  # This calculates the standard deviation of all the numbers in the nested list

    return average, total_average, variance, total_variance, std_dev, total_std_dev