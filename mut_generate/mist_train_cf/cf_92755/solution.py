"""
QUESTION:
Implement a function named merge_sort that sorts an array of numbers in ascending order. The time complexity of the algorithm should be O(nlogn) or better, and the space complexity should be O(1) or better. The algorithm should be stable, preserving the relative order of equal elements, and able to handle large input sizes without using any built-in sorting functions or libraries.
"""

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
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