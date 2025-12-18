"""
QUESTION:
Implement a function `merge_sort(arr)` that takes an array of numbers as input and returns the sorted array using only recursion. The function should divide the array into two halves, recursively sort each half, and then merge the sorted halves into a single sorted array.
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
    result = []
    left_index = 0
    right_index = 0

    while left_index < len(left_half) and right_index < len(right_half):
        if left_half[left_index] < right_half[right_index]:
            result.append(left_half[left_index])
            left_index += 1
        else:
            result.append(right_half[right_index])
            right_index += 1

    result.extend(left_half[left_index:])
    result.extend(right_half[right_index:])

    return result