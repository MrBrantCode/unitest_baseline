"""
QUESTION:
Generate a best-fit curve for a set of up to 10^6 data points represented as a list of tuples, where each tuple contains an x-coordinate and a y-coordinate. The curve can be any curve type (polynomial, exponential, logarithmic, etc.). Implement a function called `fit_curve` that takes the data points as input and returns the curve coefficients. The function should maintain a constant space complexity of O(1).
"""

import numpy as np

def fit_curve(data_points):
    x = [point[0] for point in data_points]
    y = [point[1] for point in data_points]
    
    # Fit a polynomial curve of degree 2
    coefficients = np.polyfit(x, y, 2)
    
    return coefficients