"""
QUESTION:
Write a function `find_median(arr)` that takes an array of integers `arr` and returns its median value. The function should handle cases where the array is empty, contains an even number of elements, and contains duplicate values.
"""

def find_median(arr):
    if len(arr) == 0:
        return None
    
    sorted_arr = sorted(arr)
    n = len(sorted_arr)
    middle = n // 2
    
    if n % 2 == 1:  
        return sorted_arr[middle]
    else:  
        return (sorted_arr[middle-1] + sorted_arr[middle]) / 2