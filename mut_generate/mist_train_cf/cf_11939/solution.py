"""
QUESTION:
Implement a function named merge_sort_one_iteration that takes a list of integers as input and returns a sorted list of integers. The function should sort the input list in one iteration with a time complexity of O(nlogn) and is allowed to use extra space.
"""

def merge_sort_one_iteration(arr):
    if len(arr) <= 1:
        return arr

    # Divide the array into smaller sub-arrays
    sub_arrays = [[x] for x in arr]

    # Merge pairs of adjacent sub-arrays
    while len(sub_arrays) > 1:
        merged = []
        for i in range(0, len(sub_arrays), 2):
            if i + 1 < len(sub_arrays):
                merged.append(merge(sub_arrays[i], sub_arrays[i + 1]))
            else:
                merged.append(sub_arrays[i])
        sub_arrays = merged

    return sub_arrays[0]


def merge(left, right):
    result = []
    i, j = 0, 0

    # Merge smaller elements first
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # If there are remaining elements in either the left or right sub-array, append them to the result
    result.extend(left[i:])
    result.extend(right[j:])

    return result