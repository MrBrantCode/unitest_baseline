"""
QUESTION:
Define a function `calculate_statistical_significance` that takes as input the size of the test set and the error rate, and returns the statistical significance of the results. Assume a confidence level of 95% and a margin of error of 5%.
"""

import math

def calculate_statistical_significance(test_set_size, error_rate):
    # assume a confidence level of 95% and a margin of error of 5%
    confidence_level = 0.95
    margin_of_error = 0.05

    # calculate the standard error
    standard_error = math.sqrt((error_rate * (1 - error_rate)) / test_set_size)

    # calculate the z-score
    z_score = (margin_of_error / standard_error)

    # calculate the statistical significance
    statistical_significance = 1 - (1 - confidence_level) / 2

    return statistical_significance