"""
QUESTION:
Create a function named `check_sort_progression` that determines whether an input array is sorted in ascending or descending order and/or forms a valid arithmetic or geometric progression. The array may represent an increasing or decreasing progression, and the function should be able to identify all these conditions. The function should return a string describing the properties of the input array.
"""

def check_sort_progression(arr):
    length = len(arr)
    if length == 0:
        return 'Array is empty'
    if length == 1:
        return 'Array is sorted'

    is_arithmetic = all(arr[i] - arr[i-1] == arr[1] - arr[0] for i in range(2, length))
    if is_arithmetic:
        if arr[1] - arr[0] > 0:
            return 'Array is sorted in ascending order and forms an arithmetic progression'
        else:
            return 'Array is sorted in descending order and forms an arithmetic progression'

    is_geometric = all(arr[i] / arr[i-1] == arr[1] / arr[0] for i in range(2, length))
    if is_geometric:
        if arr[1] / arr[0] > 1:
            return 'Array forms a geometric progression with increasing trend'
        else:
            return 'Array forms a geometric progression with decreasing trend'
        
    is_sorted_asc = all(arr[i] >= arr[i-1] for i in range(1, length))
    is_sorted_desc = all(arr[i] <= arr[i-1] for i in range(1, length))

    if is_sorted_asc:
        return 'Array is sorted in ascending order'
    elif is_sorted_desc:
        return 'Array is sorted in descending order'
    else:
        return 'Array is not sorted and does not form a geometric or arithmetic progression'