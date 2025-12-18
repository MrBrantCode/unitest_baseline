"""
QUESTION:
Calculate the number of test samples required to achieve a statistically meaningful error rate in a binary classification problem. The function should take two parameters: the predicted error rate `p` and the desired width of the confidence interval. The function should return the estimated number of test samples `n` based on the formula `n = (1.96 * sqrt((p * (1-p))))**2 / width**2`. Assume the confidence interval is 95% and the error rate `p` is a value between 0 and 1.
"""

import math

def calculate_test_samples_required(p, width):
    n = math.ceil((1.96 * math.sqrt((p * (1-p))))**2 / width**2)
    return n