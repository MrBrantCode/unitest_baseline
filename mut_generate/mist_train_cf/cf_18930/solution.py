"""
QUESTION:
Implement a function named merge_sort that sorts an array of integers in descending order and removes any duplicate elements. The function should have a time complexity of O(n log n) and should not use any built-in sorting functions.
"""

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] > right[j]:
            result.append(left[i])
            i += 1
        elif left[i] < right[j]:
            result.append(right[j])
            j += 1
        else:  # handling duplicate elements
            result.append(left[i])
            i += 1
            j += 1
    
    while i < len(left):
        result.append(left[i])
        i += 1
    
    while j < len(right):
        result.append(right[j])
        j += 1
    
    return result