"""
QUESTION:
Write a function `find_median(arr)` that accepts an integer array `arr` and returns its median value. The function should handle cases when the array contains an even number of elements, is empty, or contains duplicate values. The function should implement a sorting approach to find the median.
"""

def find_median(arr):
    if not arr:  
        return None

    arr.sort()  

    length = len(arr)
    mid_index = length // 2

    if length % 2 == 0:  
        return (arr[mid_index - 1] + arr[mid_index]) / 2.0

    return arr[mid_index]  