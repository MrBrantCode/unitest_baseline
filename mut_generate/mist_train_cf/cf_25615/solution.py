"""
QUESTION:
Write a function `get_median` that calculates the median of the elements in a given array of integers. The array can contain an even or odd number of elements. The function should return the median value as a float. The array is not guaranteed to be sorted.
"""

def get_median(arr):
    sorted_arr = sorted(arr)
    length = len(sorted_arr)
    if length % 2 == 0:
        median1 = sorted_arr[length // 2 - 1]
        median2 = sorted_arr[length // 2]
        median = (median1 + median2) / 2
    else:
        median = sorted_arr[(length - 1) // 2]
    return median