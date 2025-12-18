"""
QUESTION:
Create a function `merge_sort(arr)` that takes a list of integers as input and returns the list sorted in descending order, ignoring any duplicate values, and having a time complexity of O(nlogn). The function should not use any built-in sorting functions or libraries.
"""

def merge_sort(arr):
    arr = list(set(arr))  # Remove duplicates
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)
    
    return merge(left_half, right_half)

def merge(left, right):
    result = []
    i = 0
    j = 0
    
    while i < len(left) and j < len(right):
        if left[i] > right[j]:
            result.append(left[i])
            i += 1
        elif left[i] < right[j]:
            result.append(right[j])
            j += 1
        else:
            i += 1
            j += 1
    
    while i < len(left):
        result.append(left[i])
        i += 1
    
    while j < len(right):
        result.append(right[j])
        j += 1
    
    return result