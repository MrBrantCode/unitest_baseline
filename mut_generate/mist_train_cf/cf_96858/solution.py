"""
QUESTION:
Implement the `merge_sort` function that sorts a given list of numbers in descending order without using any built-in sorting functions or libraries. The function should have a time complexity of O(n log n) and a space complexity of O(log n).
"""

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    # Divide the list into two halves
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Recursively sort the two halves
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    # Merge the sorted halves
    return merge(left_half, right_half)


def merge(left_half, right_half):
    merged = []
    i = 0
    j = 0

    # Compare elements from both halves and merge them in descending order
    while i < len(left_half) and j < len(right_half):
        if left_half[i] >= right_half[j]:
            merged.append(left_half[i])
            i += 1
        else:
            merged.append(right_half[j])
            j += 1

    # Append the remaining elements of the left half (if any)
    while i < len(left_half):
        merged.append(left_half[i])
        i += 1

    # Append the remaining elements of the right half (if any)
    while j < len(right_half):
        merged.append(right_half[j])
        j += 1

    return merged