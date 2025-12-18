"""
QUESTION:
Write a function `find_median` that takes an array of integers as input and returns the median value of the array rounded to the nearest integer. The function must not sort the input array to find the median.
"""

def entance(arr):
    arr_length = len(arr)
    sorted_arr = sorted(arr)
    
    if arr_length % 2 == 1:
        median_index = arr_length // 2
        median = sorted_arr[median_index]
    else:
        median_index_1 = arr_length // 2 - 1
        median_index_2 = arr_length // 2
        median = (sorted_arr[median_index_1] + sorted_arr[median_index_2]) / 2
    
    return round(median)