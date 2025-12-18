"""
QUESTION:
Implement a function called `merge_sort` that takes an array of integers as input and returns the array sorted in ascending order. The function must have a time complexity of O(n log n) and a space complexity of O(n). Note that this implementation should be recursive, as the use of loops or iteration constructs is not allowed.
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