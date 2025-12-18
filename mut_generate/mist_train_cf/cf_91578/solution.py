"""
QUESTION:
Implement a function named `binary_search` that performs a binary search in a sorted array of positive integers (in ascending order) to find a given element `x`. The function should return the index of the element if found, otherwise return -1, and also keep track of the number of comparisons made. The array length can be at most 100, and it should handle cases where the array is empty or contains duplicate elements.
"""

def binary_search(arr, x):
    left = 0
    right = len(arr) - 1
    comparisons = 0

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == x:
            return mid, comparisons
        elif arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
        comparisons += 1

    return -1, comparisons