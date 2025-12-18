"""
QUESTION:
Write a function `joint_normal_probability` that calculates the probability that a point from a joint-normal Gaussian distribution falls within a square grid cell centered at (0,0). The function should take the standard deviations of the two variables (σ1 and σ2) and the side length of the square grid cell (a) as input, and return the probability in terms of the error function (erf()). Assume the variables are uncorrelated and zero-mean.
"""

import math

def joint_normal_probability(sigma1, sigma2, a):
    """
    Calculate the probability that a point from a joint-normal Gaussian distribution falls within a square grid cell centered at (0,0).
    
    Parameters:
    sigma1 (float): Standard deviation of variable 1
    sigma2 (float): Standard deviation of variable 2
    a (float): Side length of the square grid cell
    
    Returns:
    float: Probability in terms of the error function (erf())
    """
    
    # Calculate the probability using the cumulative distribution function (CDF) of the standard normal distribution
    prob = (math.erf(a/(sigma1 * math.sqrt(2))) - math.erf(-a/(sigma1 * math.sqrt(2)))) / 2
    
    # Since the variables are independent, return the square of the probability
    return prob ** 2