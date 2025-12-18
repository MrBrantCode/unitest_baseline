"""
QUESTION:
Calculate the Coefficient of Variation for a given list of numbers. The function should take a list of numerical inputs and return the coefficient of variation calculated as the standard deviation divided by the mean.
"""

import statistics as stats

def calculate_coefficient_of_variation(data):
    """
    Calculate the Coefficient of Variation for a given list of numbers.
    
    Args:
        data (list): A list of numerical inputs.
    
    Returns:
        float: The Coefficient of Variation calculated as the standard deviation divided by the mean.
    """
    mean_data = stats.mean(data)
    std_dev_data = stats.stdev(data)
    cv_data = std_dev_data / mean_data
    return cv_data