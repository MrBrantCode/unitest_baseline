"""
QUESTION:
Write a function called `geometric_mean` that takes a list of numbers as input and returns the geometric mean of the numbers in the list. The geometric mean is the nth root of the product of n numbers.
"""

import math
import numpy

def geometric_mean(num_list):
    product = numpy.prod(num_list)
    gm = pow(product, (1.0/len(num_list)))
    return gm