"""
QUESTION:
Write a function `median(arr)` that calculates the median of a given array `arr` without using any built-in functions or libraries for sorting or calculating the length of the array. The function should have a time complexity of O(nlogn) or better. 

The function should first sort the array in ascending order. Then, if the length of the array is odd, the median is the middle element. If the length is even, the median is the average of the two middle elements. 

Note: You can define any additional helper functions as needed.
"""

def partition(arr, low, high):
    i = low - 1
    pivot = arr[high]

    for j in range(low, high):
        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quickselect(arr, low, high, k):
    if low == high:
        return arr[low]
    
    pivot_index = partition(arr, low, high)
    if k == pivot_index:
        return arr[k]
    elif k < pivot_index:
        return quickselect(arr, low, pivot_index - 1, k)
    else:
        return quickselect(arr, pivot_index + 1, high, k)


def median(arr):
    n = len(arr)
    if n % 2 == 1:
        return quickselect(arr, 0, n - 1, n // 2)
    else:
        return (quickselect(arr, 0, n - 1, n // 2) + quickselect(arr, 0, n - 1, n // 2 - 1)) / 2