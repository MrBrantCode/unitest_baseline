"""
QUESTION:
Implement a function called `merge_sort` that sorts a list of integers in ascending order without using any built-in sorting functions or data structures. The function should have a time complexity of O(nlogn) and should handle duplicate integers and negative integers correctly. The input list will contain up to 100,000 integers ranging from -1,000,000 to 1,000,000.
"""

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)

def merge(left, right):
    merged = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
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