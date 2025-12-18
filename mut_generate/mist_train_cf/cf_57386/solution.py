"""
QUESTION:
Given the coefficient of determination (R-squared) between the number of calls made by terns and the number of nesting sites is 0.71, write a function `tern_correlation` that calculates the possible correlation coefficients between the two variables. Assume the correlation coefficient can be either positive or negative depending on the direction of the relationship.
"""

import math

def tern_correlation(r_squared):
    """
    Calculate the possible correlation coefficients given the coefficient of determination (R-squared).
    
    Parameters:
    r_squared (float): The coefficient of determination (R-squared) between two variables.
    
    Returns:
    tuple: A tuple containing the possible correlation coefficients.
    """
    r = math.sqrt(r_squared)
    return -r, r