"""
QUESTION:
Write a function named `calculate_t_statistic` that calculates the t-statistic for the difference between two alphas from a panel regression. The function should take the alphas and their standard errors as input, and return the t-statistic and its standard error. The function should assume that the portfolios are independent.
"""

import math

def calculate_t_statistic(alpha_low, alpha_high, std_err_low, std_err_high):
    """
    Calculate the t-statistic for the difference between two alphas from a panel regression.

    Parameters:
    alpha_low (float): Alpha estimate for the low portfolio.
    alpha_high (float): Alpha estimate for the high portfolio.
    std_err_low (float): Standard error of the alpha estimate for the low portfolio.
    std_err_high (float): Standard error of the alpha estimate for the high portfolio.

    Returns:
    t_statistic (float): The t-statistic for the difference between the two alphas.
    std_err_diff (float): The standard error of the difference between the two alphas.
    """
    
    # Calculate the standard error of the difference
    std_err_diff = math.sqrt(std_err_low**2 + std_err_high**2)

    # Calculate the t-statistic
    t_statistic = (alpha_low - alpha_high) / std_err_diff

    return t_statistic, std_err_diff