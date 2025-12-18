"""
QUESTION:
Estimate the marginal effect of a Poisson regression model with individual fixed effects. 

The function, `estimate_marginal_effect`, should calculate the marginal effect of a covariate, often referred to as the Incidence Rate Ratio, which represents a percentage change in the response for each unit increase in the predictor, holding other predictors constant. The function should take a Poisson regression model with individual fixed effects as input.
"""

import numpy as np

def estimate_marginal_effect(coefficients, covariate_index):
    """
    Calculate the marginal effect of a covariate in a Poisson regression model.

    Parameters:
    coefficients (list): A list of coefficients from the Poisson regression model.
    covariate_index (int): The index of the covariate for which to calculate the marginal effect.

    Returns:
    float: The marginal effect of the specified covariate, representing a percentage change in the response for each unit increase in the predictor.
    """
    # Calculate the marginal effect as the exponentiated coefficient of the covariate
    marginal_effect = np.exp(coefficients[covariate_index])
    return marginal_effect