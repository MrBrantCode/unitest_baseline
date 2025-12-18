"""
QUESTION:
Write a function `best_fit_line` that calculates and returns the equation of the best-fit line for a given set of 2D points. The function should take a list of tuples, where each tuple represents an (x, y) point, and return a string representing the equation of the best-fit line in the format "y = mx + c". The function should use a linear regression model to calculate the slope (m) and intercept (c) of the best-fit line.
"""

import numpy as np

def best_fit_line(points):
    """
    Calculate and return the equation of the best-fit line for a given set of 2D points.
    
    Parameters:
    points (list of tuples): A list of tuples, where each tuple represents an (x, y) point.
    
    Returns:
    str: A string representing the equation of the best-fit line in the format "y = mx + c".
    """
    x = np.array([x[0] for x in points])
    y = np.array([y[1] for y in points])
    
    m, c = np.polyfit(x, y, 1)
    
    return "y = {:.2f}x + {:.2f}".format(m,c)