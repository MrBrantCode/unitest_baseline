"""
QUESTION:
Design an algorithm that implements the merge sort function to sort an array of integers in ascending order. The function should have a time complexity of O(n log n) and a space complexity of O(n). The algorithm should handle duplicate integers, negative integers, and the case where the array contains only negative integers. 

The algorithm should be implemented using a recursive approach with two functions: merge and mergeSort. The merge function should take two sorted arrays and return a new sorted array containing all elements from both arrays. The mergeSort function should take an array and return a new sorted array. The original array should remain unchanged.
"""

def merge(left, right):
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
            
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def entrance(array):
    if len(array) <= 1:
        return array
    
    mid = len(array) // 2
    left = array[:mid]
    right = array[mid:]
    
    left = entrance(left)
    right = entrance(right)
    
    return merge(left, right)