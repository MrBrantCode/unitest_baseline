"""
QUESTION:
Implement a function `merge_sort(arr)` that takes an array of integers as input and returns the sorted array in ascending order. The function should have a time complexity of O(n log n) and use a constant amount of extra space. The function should be implemented recursively and be able to handle arrays of size up to 10^6.
"""

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    # Split the array into two halves
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    
    # Recursively sort the left and right halves
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)
    
    # Merge the sorted halves
    return merge(left_half, right_half)

def merge(left_half, right_half):
    merged = []
    i = 0
    j = 0
    
    # Merge the two halves by comparing elements
    while i < len(left_half) and j < len(right_half):
        if left_half[i] < right_half[j]:
            merged.append(left_half[i])
            i += 1
        else:
            merged.append(right_half[j])
            j += 1
    
    # Append the remaining elements from either half
    while i < len(left_half):
        merged.append(left_half[i])
        i += 1
    
    while j < len(right_half):
        merged.append(right_half[j])
        j += 1
    
    return merged