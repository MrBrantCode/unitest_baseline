"""
QUESTION:
Implement a function `reorderArray` that takes an array of integers as input and returns the array with the numbers rearranged in descending order. The function should have a time complexity of O(n log n), where n is the length of the input array. You may not use any built-in sorting functions or methods. The input array will always contain at least one element and may contain negative numbers and duplicates.
"""

def merge(left, right):
    merged = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] >= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged

def reorderArray(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = reorderArray(arr[:mid])
    right = reorderArray(arr[mid:])
    return merge(left, right)