"""
QUESTION:
Implement the merge_sort function to sort an array of integers, including negative numbers, with a time complexity of O(n log n). The function should take one parameter, arr, which is the input array of integers. The function should return the sorted array.
"""

def entrance(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    
    left_half = entrance(left_half)
    right_half = entrance(right_half)
    
    return merge(left_half, right_half)


def merge(left, right):
    result = []
    i = j = 0
    
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