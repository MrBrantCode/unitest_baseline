"""
QUESTION:
Implement a sorting algorithm from scratch that sorts an array of integers in ascending order. The function, named `merge_sort(arr)`, should have a time complexity of O(n log n) and a space complexity of O(1), where n is the number of elements in the array. Do not use any built-in sorting functions or libraries.
"""

def entance(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    
    entance(left_half)
    entance(right_half)
    
    merge(arr, left_half, right_half)
    return arr

def merge(arr, left_half, right_half):
    i = j = k = 0
    while i < len(left_half) and j < len(right_half):
        if left_half[i] < right_half[j]:
            arr[k] = left_half[i]
            i += 1
        else:
            arr[k] = right_half[j]
            j += 1
        k += 1
    
    while i < len(left_half):
        arr[k] = left_half[i]
        i += 1
        k += 1
    
    while j < len(right_half):
        arr[k] = right_half[j]
        j += 1
        k += 1