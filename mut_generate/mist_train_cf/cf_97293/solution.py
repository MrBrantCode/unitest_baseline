"""
QUESTION:
Implement a function named `merge_sort` that takes an array of integers as input and returns the array sorted in descending order without using any built-in sorting functions or methods. The function must have a time complexity of O(n log n), where n is the length of the array.
"""

def merge_sort(arr):
    # Base case: if the array has only one element, it is already sorted
    if len(arr) <= 1:
        return arr

    # Split the array into two halves
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Recursively sort the two halves
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    # Merge the sorted halves
    return merge(left_half, right_half)


def merge(left, right):
    result = []

    # Compare elements from both halves and add them to the result in descending order
    while left and right:
        if left[0] >= right[0]:
            result.append(left[0])
            left = left[1:]
        else:
            result.append(right[0])
            right = right[1:]

    # Add any remaining elements from the left or right halves
    result.extend(left)
    result.extend(right)

    return result