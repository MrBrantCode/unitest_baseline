"""
QUESTION:
Write a function `find_median(arr)` that calculates the median of all elements in a given array and returns it rounded to the nearest integer. The function should find the median without sorting the entire array, but for the sake of this problem, a sorting approach is acceptable.
"""

def find_median(arr):
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