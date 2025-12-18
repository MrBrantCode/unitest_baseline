"""
QUESTION:
Create a function named binary_search that implements a binary search in an array of positive integers in ascending order. The function should take an array arr and an element x as parameters, and return a tuple containing the index of the element if found and the number of comparisons made. If the element is not found, the function should return -1 and the number of comparisons made. The length of the array will be less than or equal to 100, and the function should handle cases where the array is empty or contains duplicate elements.
"""

def binary_search(arr, x):
    left = 0
    right = len(arr) - 1
    comparisons = 0

    while left <= right:
        mid = (left + right) // 2
        comparisons += 1
        if arr[mid] == x:
            return mid, comparisons
        elif arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1

    return -1, comparisons