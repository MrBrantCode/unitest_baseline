"""
QUESTION:
Implement a function `merge_sort(arr)` that takes an array of integers as input and returns a new array with the integers sorted in ascending order using the Merge Sort algorithm. The input array can contain duplicate integers and is not guaranteed to be sorted initially. The function should be able to handle arrays of any length, including empty arrays and arrays with a single element.
"""

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    return merge(merge_sort(left_half), merge_sort(right_half))

def merge(left_half, right_half):
    merged = []
    left_index = 0
    right_index = 0

    while left_index < len(left_half) and right_index < len(right_half):
        if left_half[left_index] < right_half[right_index]:
            merged.append(left_half[left_index])
            left_index += 1
        else:
            merged.append(right_half[right_index])
            right_index += 1

    while left_index < len(left_half):
        merged.append(left_half[left_index])
        left_index += 1

    while right_index < len(right_half):
        merged.append(right_half[right_index])
        right_index += 1

    return merged