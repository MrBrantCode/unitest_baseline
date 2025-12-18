"""
QUESTION:
Design a method named `common_elements_with_logarithm` that takes two unsorted integer arrays `arr1` and `arr2` as input. The function should return a new array containing the elements that exist in both input arrays, with each overlapping element replaced by its natural logarithm. The solution must be efficient even for larger arrays. Note that the input arrays should only contain positive integers to avoid math domain errors.
"""

import math

def common_elements_with_logarithm(arr1, arr2):
    # Create sets from the two input arrays
    set1 = set(arr1)
    set2 = set(arr2)

    # Find the common elements and apply natural logarithm
    common_elements = [math.log(el) for el in set1 if el in set2]

    return common_elements