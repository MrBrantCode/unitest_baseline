"""
QUESTION:
Implement a function called merge_sort that sorts a given array of integers in ascending order. The function should have a time complexity of O(n log n), not use any built-in sorting functions or libraries, and be able to handle large input sizes, duplicate elements, and preserve the relative order of equal elements. The function should be in-place and adaptive, meaning it does not use additional memory proportional to the input size and takes advantage of any pre-existing order in the data.
"""

def merge_sort(arr):
    if len(arr) <= 1:
        return
    
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    
    merge_sort(left)
    merge_sort(right)
    
    merge(arr, left, right)

def merge(arr, left, right):
    i = j = k = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1
    
    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1
    
    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1