"""
QUESTION:
Write a function named `weibull_hazard_ratio_ci` that calculates the 95% confidence interval for the hazard ratio from a Weibull regression model output. The function should take in three parameters: `beta_estimate`, `beta_standard_error`, and `shape`. The function should return the lower and upper limits of the 95% confidence interval for the hazard ratio. Assume that the hazard ratio is given by the formula HR = exp(-beta)^shape.
"""

import math

def weibull_hazard_ratio_ci(beta_estimate, beta_standard_error, shape):
    """
    Calculate the 95% confidence interval for the hazard ratio from a Weibull regression model output.

    Parameters:
    beta_estimate (float): The estimated beta value from the Weibull regression model.
    beta_standard_error (float): The standard error of the estimated beta value.
    shape (float): The shape parameter of the Weibull distribution.

    Returns:
    tuple: A tuple containing the lower and upper limits of the 95% confidence interval for the hazard ratio.
    """
    beta_lower_limit = beta_estimate - 1.96 * beta_standard_error
    beta_upper_limit = beta_estimate + 1.96 * beta_standard_error

    hr_lower_limit = math.exp(-beta_upper_limit) ** shape
    hr_upper_limit = math.exp(-beta_lower_limit) ** shape

    return hr_lower_limit, hr_upper_limit