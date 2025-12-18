"""
QUESTION:
Create a function `f(x)` that takes an input array of x values and returns an array of the squared values of x. The function should only consider x values that are multiples of 3 and less than 9. The resulting array should only include values greater than 0 and less than or equal to 100, sorted in descending order, and converted to integers. The function should use NumPy and the input range of x values is from -10 to 10 with a step size of 0.5.
"""

import numpy as np

def entrance(x):
    return np.sort(np.array([int(i**2) for i in x if i % 3 == 0 and i < 9 and 0 < i**2 <= 100]))[::-1]