"""
QUESTION:
Create a function `merge_sort(arr)` that takes an array of integers (which can be positive, negative, or both) as input and returns the sorted array using the Merge Sort algorithm. The function should have a time complexity of O(nlogn).
"""

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)
    
    return merge(left_half, right_half)

def merge(left_arr, right_arr):
    merged = []
    i = 0
    j = 0
    
    while i < len(left_arr) and j < len(right_arr):
        if left_arr[i] <= right_arr[j]:
            merged.append(left_arr[i])
            i += 1
        else:
            merged.append(right_arr[j])
            j += 1
    
    merged += left_arr[i:]
    merged += right_arr[j:]
    
    return merged