"""
QUESTION:
Write a function `vecm_half_life` that calculates the half-life of a VECM model given the speed of adjustment parameter λ. The half-life is the number of time periods it takes for a short-term shock to dissipate and converge to the long-term equilibrium. Assume that λ > 0.
"""

import numpy as np

def vecm_half_life(lambda_):
    """
    Calculate the half-life of a VECM model given the speed of adjustment parameter λ.
    
    Parameters:
    lambda_ (float): The speed of adjustment parameter. It is assumed to be greater than 0.
    
    Returns:
    float: The half-life of the VECM model.
    """
    return np.log(2) / lambda_