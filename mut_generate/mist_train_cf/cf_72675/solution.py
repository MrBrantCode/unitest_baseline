"""
QUESTION:
Write a function `find_means(arr)` that takes an array of positive integers as input and returns the harmonic, geometric, and arithmetic means of the array, with the result rounded to the standard floating-point precision. The function should use the formulas for the harmonic mean (reciprocal of the arithmetic mean of the reciprocals), geometric mean (n-th root of the product of all elements), and arithmetic mean (sum of elements divided by the number of elements).
"""

import math
import statistics
import numpy as np

def find_means(arr):
    harmonic_mean = statistics.harmonic_mean(arr)
    geometric_mean = np.prod(np.array(arr))**(1.0/len(arr))
    arithmetic_mean = sum(arr) / float(len(arr))
    
    return harmonic_mean, geometric_mean, arithmetic_mean