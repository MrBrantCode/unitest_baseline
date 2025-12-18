"""
QUESTION:
Write a function named `insertion_sort` that sorts a list of integers using binary search-based insertion sort. The function should take a list of integers as input and return the sorted list. The input list can contain duplicate values and is not guaranteed to be sorted. The function should use a helper function named `binary_search` to find the position where each element should be inserted among the already sorted elements.
"""

def binary_search(arr, key, start, end):
    if end <= start:
        if key > arr[start]:
            return start + 1
        else:
            return start
    mid = (start + end) // 2
    if key == arr[mid]:
        return mid + 1
    if key < arr[mid]:
        return binary_search(arr, key, start, mid)
    return binary_search(arr, key, mid + 1, end)

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        index = binary_search(arr, key, 0, i)  # find the position where key should be inserted
        arr = arr[:index] + [key] + arr[index:i] + arr[i+1:]  # insert key at index
    return arr