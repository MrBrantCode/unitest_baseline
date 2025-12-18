"""
QUESTION:
Implement a recursive binary search function named `binary_search` that takes a sorted array of integers and a target value as input. The function should return the index of the target value if found, and -1 otherwise. The function should have a time complexity of O(log n), where n is the size of the input array, and should not use any built-in sorting or searching functions. The input array may be empty, contain duplicate elements, or negative integers.
"""

def binary_search(arr, target):
    def binary_search_helper(arr, target, low, high):
        if low > high:
            return -1

        mid = (low + high) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            return binary_search_helper(arr, target, low, mid - 1)
        else:
            return binary_search_helper(arr, target, mid + 1, high)

    return binary_search_helper(arr, target, 0, len(arr) - 1)