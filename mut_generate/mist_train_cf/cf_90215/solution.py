"""
QUESTION:
Write a function named `merge_sort` that sorts an array of integers from largest to smallest using a divide and conquer approach with a time complexity of O(n log n) or better. The function should handle duplicate integers correctly, preserving their relative order in the sorted array, and should not use any built-in sorting functions or libraries.
"""

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])
    
    return merge(left_half, right_half)

def merge(left_half, right_half):
    merged = []
    i = j = 0
    
    while i < len(left_half) and j < len(right_half):
        if left_half[i] >= right_half[j]:
            merged.append(left_half[i])
            i += 1
        else:
            merged.append(right_half[j])
            j += 1
    
    while i < len(left_half):
        merged.append(left_half[i])
        i += 1
    
    while j < len(right_half):
        merged.append(right_half[j])
        j += 1
    
    return merged