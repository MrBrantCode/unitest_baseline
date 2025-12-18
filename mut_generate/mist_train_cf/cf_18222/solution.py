"""
QUESTION:
Write a function `euclidean_distance(arr1, arr2)` that calculates the Euclidean distance between two input arrays `arr1` and `arr2`. The function should return the Euclidean distance as a floating-point number. The input arrays are guaranteed to have the same length, and the time complexity of the function should not exceed O(n), where n is the number of elements in each array.
"""

import math

def euclidean_distance(arr1, arr2):
    distance = 0
    for i in range(len(arr1)):
        diff = arr1[i] - arr2[i]
        distance += diff * diff
    return math.sqrt(distance)