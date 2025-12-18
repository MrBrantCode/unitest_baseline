"""
QUESTION:
Write a function `find_kth_largest` that takes an unsorted array of unique positive integers and an integer `k` as input, and returns the kth largest element in the array. The function should run in an average time complexity of O(n), where n is the length of the array. The array can contain up to 10^5 elements, with all elements ranging from 1 to 10^9.
"""

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] >= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i+1

def quickselect(arr, low, high, k):
    if low <= high:
        pivot_index = partition(arr, low, high)
        if pivot_index == k-1:
            return arr[pivot_index]
        elif pivot_index < k-1:
            return quickselect(arr, pivot_index+1, high, k)
        else:
            return quickselect(arr, low, pivot_index-1, k)

def find_kth_largest(arr, k):
    n = len(arr)
    return quickselect(arr, 0, n-1, k)