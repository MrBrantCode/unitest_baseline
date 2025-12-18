"""
QUESTION:
Write a function `calculate_median` that takes a list of integers as input and returns its median value. The function should handle both cases when the list contains an odd or even number of elements. The input list is not guaranteed to be sorted, and the function should return a float value if the median is not an integer.
"""

def calculate_median(arr):
    arr.sort()
    length = len(arr)
    mid_index = length // 2
    if length % 2 == 0:
        median = (arr[mid_index - 1] + arr[mid_index]) / 2
    else:
        median = arr[mid_index]
    return median