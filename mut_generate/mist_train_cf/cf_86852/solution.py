"""
QUESTION:
Implement a function named `merge_sort` that takes in a list of numbers as input and returns a sorted list. The function should have a time complexity of O(n log n) and a space complexity of O(n). The `merge_sort` function should utilize a helper function named `merge` that merges two sorted lists into a single sorted list with a time complexity of O(n).
"""

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

    result.extend(left[i:])
    result.extend(right[j:])
    
    return result


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)