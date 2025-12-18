"""
QUESTION:
Implement a function called `mergeSort` that takes a list of integers as input and returns the sorted list in ascending order. The function should have a time complexity of O(n log n). The input list can be empty or contain duplicate integers.
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
    
    while left and right:
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    
    result.extend(left)
    result.extend(right)
    
    return result