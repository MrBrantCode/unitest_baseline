"""
QUESTION:
Implement a function named `merge_sort` that takes an array of distinct integers as input and returns a new array with the same integers in ascending order. The function should not use any built-in sorting functions or libraries. The input array will contain at least 2 numbers and at most 10^6 numbers, and all numbers will be in the range of -10^9 to 10^9. The function should have a time complexity of O(n log n).
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

def merge(left, right):
    result = []
    i = 0
    j = 0
    
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    while i < len(left):
        result.append(left[i])
        i += 1
    
    while j < len(right):
        result.append(right[j])
        j += 1
    
    return result