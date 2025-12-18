"""
QUESTION:
Write a function `gradient_sum` that takes a 3-dimensional array as input. The function should first sum the array along the third axis, then calculate the gradient of the resulting 2-dimensional array. The function should print each element in the gradient array and return the gradient array. The time complexity of the solution should be as low as possible.
"""

import numpy as np

def gradient_sum(arr):
    array = np.array(arr)
    sum_array = np.sum(array, axis=2)
    gradient = np.gradient(sum_array)
    for g in gradient:
        print(g)
    return gradient