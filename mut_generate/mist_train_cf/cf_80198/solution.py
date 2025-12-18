"""
QUESTION:
Write a function `merge_sort(arr)` that sorts an array of integers in ascending order using the merge sort algorithm. The function should recursively divide the array into two halves until each sub-array contains only one element, and then merge the sub-arrays back together in sorted order. Use the Master Theorem to determine the time complexity of the function.

Restrictions: The input array can contain duplicate elements, and the function should be able to handle arrays of any size. The function should not use any built-in sorting functions or libraries.
"""

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    return merge(left_half, right_half)

def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    merged += left[left_index:]
    merged += right[right_index:]

    return merged