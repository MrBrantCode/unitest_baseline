"""
QUESTION:
Write a function `generate_best_fit_line` that takes a list of tuples, where each tuple contains two values: the x-coordinate and the y-coordinate, and returns the slope and intercept of the best-fit line for the given data points. The function should have a time complexity of O(n), where n is the number of data points, and should be able to handle up to 10^6 data points.
"""

import numpy as np

def generate_best_fit_line(data_points):
    x_coordinates, y_coordinates = zip(*data_points)
    coefficients = np.polyfit(x_coordinates, y_coordinates, 1)
    slope, intercept = coefficients

    return slope, intercept