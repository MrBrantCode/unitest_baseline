"""
QUESTION:
Implement a function called `merge_sort` that takes an array of integers as input and returns the sorted array in ascending order. The input array will contain at least 10,000 elements. The function should use the merge sort algorithm to sort the array, splitting it into two halves recursively until the base case is reached (array length <= 1) and then merging the sorted halves back together in ascending order.
"""

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    return merge(left_half, right_half)

def merge(left_half, right_half):
    merged = []
    left_index, right_index = 0, 0

    while left_index < len(left_half) and right_index < len(right_half):
        if left_half[left_index] < right_half[right_index]:
            merged.append(left_half[left_index])
            left_index += 1
        else:
            merged.append(right_half[right_index])
            right_index += 1

    merged.extend(left_half[left_index:])
    merged.extend(right_half[right_index:])

    return merged