"""
QUESTION:
Write a function named `generate_best_fit_line` that takes a list of tuples representing data points in 2D space and returns the slope and intercept of the best-fit line. Each tuple in the input list should contain an x-coordinate and a y-coordinate. The function should have a time complexity of O(n), where n is the number of data points.
"""

import numpy as np

def generate_best_fit_line(data_points):
    x_coordinates, y_coordinates = zip(*data_points)
    coefficients = np.polyfit(x_coordinates, y_coordinates, 1)
    slope, intercept = coefficients

    return slope, intercept