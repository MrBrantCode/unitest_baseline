"""
QUESTION:
Implement a function named `merge_sort` that sorts a large array with a time complexity of O(n log n) and uses a constant amount of additional memory. The function should take an array of integers as input and return a sorted array. The array should be split into halves recursively until the base case of an array with one or zero elements is reached. Then, merge the sorted subarrays in a sorted manner.
"""

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)


def merge(left, right):
    merged = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    while i < len(left):
        merged.append(left[i])
        i += 1

    while j < len(right):
        merged.append(right[j])
        j += 1

    return merged