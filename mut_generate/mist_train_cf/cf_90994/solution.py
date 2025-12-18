"""
QUESTION:
Write a function named `merge_sort` that takes an array of integers as input, sorts it in increasing order, and returns the sorted array. The function should not use any built-in sorting functions or libraries. The time complexity should be less than O(n^2) and the space complexity should be less than O(n).
"""

def merge_sort(arr):
    # Base case: if the array has only one element or is empty, return it
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
    merged = []
    i = j = 0

    # Compare the elements from both halves and add them to the merged list in sorted order
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    # Add the remaining elements from the left half
    while i < len(left):
        merged.append(left[i])
        i += 1

    # Add the remaining elements from the right half
    while j < len(right):
        merged.append(right[j])
        j += 1

    return merged