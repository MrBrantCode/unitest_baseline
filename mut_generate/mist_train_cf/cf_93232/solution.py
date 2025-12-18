"""
QUESTION:
Implement a function named `merge_sort` that takes a list of integers as input and returns the list sorted in ascending order without using any built-in sorting functions or libraries.
"""

def merge_sort(arr):
    # Base case: if the list has 0 or 1 element, it is already sorted
    if len(arr) <= 1:
        return arr

    # Split the list into two halves
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Recursively sort each half
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    # Merge the two sorted halves
    sorted_arr = []
    i = j = 0
    while i < len(left_half) and j < len(right_half):
        if left_half[i] < right_half[j]:
            sorted_arr.append(left_half[i])
            i += 1
        else:
            sorted_arr.append(right_half[j])
            j += 1

    # Add any remaining elements from the left half
    while i < len(left_half):
        sorted_arr.append(left_half[i])
        i += 1

    # Add any remaining elements from the right half
    while j < len(right_half):
        sorted_arr.append(right_half[j])
        j += 1

    return sorted_arr