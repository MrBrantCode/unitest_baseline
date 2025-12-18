"""
QUESTION:
Implement the merge_sort function, which takes an array of integers as input and returns the array sorted in descending order (largest to smallest) with a time complexity of O(n log n) or better.
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

def merge(left_half, right_half):
    merged_arr = []
    i = j = 0
    
    while i < len(left_half) and j < len(right_half):
        if left_half[i] > right_half[j]:
            merged_arr.append(left_half[i])
            i += 1
        else:
            merged_arr.append(right_half[j])
            j += 1
    
    while i < len(left_half):
        merged_arr.append(left_half[i])
        i += 1
    
    while j < len(right_half):
        merged_arr.append(right_half[j])
        j += 1
    
    return merged_arr