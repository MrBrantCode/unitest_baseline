"""
QUESTION:
Write a function named `calculate_median` that takes an array of numbers (including floating numbers, negative numbers, and complex numbers) as input. The function should handle cases where the array is empty or contains duplicate values. The array should be sorted based on the absolute values of its elements. If the array size is even, the median should be the mean of the two middle values; if the array size is odd, the median should be the middle value.
"""

import cmath

def calculate_median(array):
    if len(array) == 0:
        return "The array is empty."

    array.sort(key=abs)
    
    if len(array) % 2 == 0:
        median1 = array[len(array) // 2]
        median2 = array[len(array) // 2 - 1]
        median = (median1 + median2) / 2
    else:
        median = array[len(array) // 2]

    return median