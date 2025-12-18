"""
QUESTION:
Write a function `top_k_largest` that takes a list `arr` and an integer `k` as input, where `k` is a positive integer. The function should return the `k`th largest number in the list. The list can contain duplicates and can have a length of up to 10^6 elements. The function should have a time complexity of O(n) and should not use any built-in sorting functions or libraries, and should only use a single loop to iterate through the list.
"""

def partition(arr, low, high):
    pivot = arr[high]
    i = low
    for j in range(low, high):
        if arr[j] <= pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[high] = arr[high], arr[i]
    return i

def quickselect(arr, low, high, k):
    if low < high:
        pivot_index = partition(arr, low, high)
        if pivot_index == len(arr) - k:
            return arr[pivot_index]
        elif pivot_index < len(arr) - k:
            return quickselect(arr, pivot_index + 1, high, k)
        else:
            return quickselect(arr, low, pivot_index - 1, k)

def top_k_largest(arr, k):
    return quickselect(arr, 0, len(arr) - 1, k)