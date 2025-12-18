"""
QUESTION:
Implement a function `merge_sort(arr)` that recursively sorts the given array of integers in ascending order with a time complexity of O(n log n) without using any built-in sorting functions or data structures. The input array can contain both positive and negative integers.
"""

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_arr = arr[:mid]
    right_arr = arr[mid:]

    sorted_left_arr = merge_sort(left_arr)
    sorted_right_arr = merge_sort(right_arr)

    return merge(sorted_left_arr, sorted_right_arr)

def merge(left_arr, right_arr):
    result = []
    i = j = 0

    while i < len(left_arr) and j < len(right_arr):
        if left_arr[i] <= right_arr[j]:
            result.append(left_arr[i])
            i += 1
        else:
            result.append(right_arr[j])
            j += 1

    result.extend(left_arr[i:])
    result.extend(right_arr[j:])

    return result