"""
QUESTION:
Implement a function called `sort_integer_list` that takes a list of integers as input and returns a sorted list of integers in ascending order. The function should handle duplicate elements and maintain their relative order. The time complexity of the function should be O(n log n) and the space complexity should be O(1), without using any built-in sorting functions or libraries, or additional data structures.
"""

def sort_integer_list(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = sort_integer_list(arr[:mid])
    right = sort_integer_list(arr[mid:])
    return merge(left, right)

def merge(left, right):
    merged = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    
    while i < len(left):
        merged.append(left[i])
        i += 1
    
    while j < len(right):
        merged.append(right[j])
        j += 1
    
    return merged