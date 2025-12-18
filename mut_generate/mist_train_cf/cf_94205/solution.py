"""
QUESTION:
Develop a function `merge_sort(arr)` that takes an array of numbers as input and returns the array sorted in descending order using recursion. The function should split the array into two halves, recursively sort each half, and then merge the sorted halves back together. The merge step should compare elements from both halves and append them to the merged list in descending order.
"""

def merge_sort(arr):
    # Base case: an empty array or an array with a single element is already sorted
    if len(arr) <= 1:
        return arr

    # Split the array into two halves
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Recursively sort the two halves
    left_sorted = merge_sort(left_half)
    right_sorted = merge_sort(right_half)

    # Merge the sorted halves
    return merge(left_sorted, right_sorted)


def merge(left, right):
    merged = []
    left_index = right_index = 0

    # Compare elements from both halves and append them to the merged list in descending order
    while left_index < len(left) and right_index < len(right):
        if left[left_index] > right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    # Append any remaining elements from the left or right halves
    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1
    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1

    return merged