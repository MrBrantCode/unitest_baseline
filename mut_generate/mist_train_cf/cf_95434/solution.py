"""
QUESTION:
Implement a function `merge_sort` that takes a list of integers as input, removes duplicate elements, and returns the sorted list in descending order with a time complexity of O(n log n) without using any built-in sorting functions.
"""

def merge_sort(arr):
    arr = list(set(arr))  # remove duplicate elements
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    
    left = merge_sort(left)
    right = merge_sort(right)
    
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