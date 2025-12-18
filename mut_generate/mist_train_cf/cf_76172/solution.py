"""
QUESTION:
Write a function `f` that calculates the 3rd standard deviation interval for a given array `a`, returning a tuple containing the start and end points of the interval. The start point is the mean of `a` minus 3 times the standard deviation of `a`, and the end point is the mean of `a` plus 3 times the standard deviation of `a`.
"""

import numpy as np

def entrance(a):
    mean = np.mean(a)
    standard_deviation = np.std(a)
    start = mean - 3*standard_deviation
    end = mean + 3*standard_deviation
    result = (start, end)
    return result