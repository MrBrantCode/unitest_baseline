"""
QUESTION:
Create a function named `binary_search` to perform recursive binary search in a sorted array of distinct elements. The function should take a sorted array `arr` and a target element `target` as input and return the index of the target element if found, or -1 if the target is not present. The function should have a time complexity of O(log n) and not use any built-in search functions, libraries, or auxiliary data structures.
"""

def binary_search(arr, target):
    def binary_search_helper(arr, target, left, right):
        if left > right:
            return -1

        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            return binary_search_helper(arr, target, left, mid - 1)
        else:
            return binary_search_helper(arr, target, mid + 1, right)

    return binary_search_helper(arr, target, 0, len(arr) - 1)