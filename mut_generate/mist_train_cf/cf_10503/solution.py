"""
QUESTION:
Design a function `merge_sort` that takes a list of integers as input and returns the sorted list. The function should have a time complexity of O(n log n) and a space complexity of O(1). Implement the sorting algorithm without using any built-in sorting functions or libraries.
"""

def merge_sort(arr):
    if len(arr) < 2:
        return arr
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    left = merge_sort(left)
    right = merge_sort(right)
    return merge(left, right)

def merge(left, right):
    result = []
    while len(left) > 0 and len(right) > 0:
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    result.extend(left)
    result.extend(right)
    return result