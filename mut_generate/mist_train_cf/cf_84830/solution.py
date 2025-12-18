"""
QUESTION:
Given a series of repeated measures of the root-mean-squared-error (RMSE) between observed values and predicted values from simulation studies, where the samples contributing to the measures are of the same size and relate to the same predicted value, write a function called `estimate_population_rmse` that takes a list of RMSE values as input and returns the estimated population RMSE, along with a measure of its variability.
"""

import numpy as np

def estimate_population_rmse(rmses):
    """
    Estimate the population RMSE and its variability.

    Parameters:
    rmses (list): A list of RMSE values.

    Returns:
    tuple: A tuple containing the estimated population RMSE and its standard deviation.
    """
    # Calculate the mean of the RMSE values
    mean_rmse = np.mean(rmses)
    
    # Calculate the standard deviation of the RMSE values
    std_rmse = np.std(rmses, ddof=1)
    
    return mean_rmse, std_rmse