"""
QUESTION:
Write a function `softmax_numerical_stability` to prove that adding the same constant to the exponent in the numerator and denominator of the softmax function does not change its output. The function should take a list of raw variables or scores `y` and an optional constant `C` as input, and return a boolean value indicating whether the output of the softmax function changes after adding `C` to the exponent.
"""

import math

def softmax_numerical_stability(y, C=None):
    if C is None:
        C = max(y)
    sum_exp_y = sum(math.exp(score) for score in y)
    sum_exp_y_with_C = sum(math.exp(score + C) for score in y)
    softmax_y = [math.exp(score) / sum_exp_y for score in y]
    softmax_y_with_C = [math.exp(score + C) / sum_exp_y_with_C for score in y]
    return math.isclose(sum(softmax_y), sum(softmax_y_with_C))