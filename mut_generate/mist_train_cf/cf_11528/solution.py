"""
QUESTION:
Write a recursive function `merge_sort(arr)` that sorts the given array of integers in descending order using the Merge Sort algorithm, and returns a tuple containing the sorted array and the total number of swaps made during the sorting process. The function should recursively divide the array into two halves until each half has one or zero elements, and then merge the sorted halves into a single sorted array. The merge step should compare elements from both halves and add the larger one to the merged array, counting the number of swaps made when an element from the right half is added before an element from the left half.
"""

def merge_sort(arr):
    # Base case: if the array has one or zero elements, it is already sorted
    if len(arr) <= 1:
        return arr, 0

    # Divide the array into two halves
    mid = len(arr) // 2
    left_half, swaps_left = merge_sort(arr[:mid])
    right_half, swaps_right = merge_sort(arr[mid:])

    # Merge the sorted halves
    sorted_arr, swaps_merge = merge(left_half, right_half)

    # Return the sorted array and the total number of swaps
    return sorted_arr, swaps_left + swaps_right + swaps_merge


def merge(left, right):
    merged = []
    swaps = 0

    i = j = 0
    while i < len(left) and j < len(right):
        # Compare the elements from both halves and add the larger one to the merged array
        if left[i] >= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
            swaps += len(left) - i  # Count the number of swaps made

    # Add the remaining elements from the left half, if any
    while i < len(left):
        merged.append(left[i])
        i += 1

    # Add the remaining elements from the right half, if any
    while j < len(right):
        merged.append(right[j])
        j += 1

    return merged, swaps