"""
QUESTION:
Write a function called `merge_sort` that takes an array of unique integers as input, sorts the array in ascending order using the merge sort algorithm, and returns the sorted array. The input array is not guaranteed to be sorted and can be of any size, but for the purpose of this problem, it will contain 10,000 unique integers between -100 and 100.
"""

def merge_sort(array):
    # Base case: if the array is empty or has only one element, it is already sorted
    if len(array) <= 1:
        return array

    # Split the array into two halves
    mid = len(array) // 2
    left_half = array[:mid]
    right_half = array[mid:]

    # Recursively sort each half
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    # Merge the sorted halves
    return merge(left_half, right_half)

def merge(left, right):
    merged = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    # Append the remaining elements of the unfinished half
    merged.extend(left[i:])
    merged.extend(right[j:])

    return merged