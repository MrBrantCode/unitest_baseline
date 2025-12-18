"""
QUESTION:
Implement a recursive function `merge_sort(arr)` that sorts an array of numbers using the merge sort algorithm. The function should take an array of numbers as input and return a sorted array. The function should recursively divide the array into two halves until the base case of an array with length 1 is reached, and then merge the sorted halves to create a sorted array.
"""

def entance(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    left_half = entance(left_half)
    right_half = entance(right_half)

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