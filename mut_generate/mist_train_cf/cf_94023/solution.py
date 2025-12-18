"""
QUESTION:
Write a function `search` that takes a sorted array `arr` and a target value `target` as input. Return the index of the target if it exists in the array, and -1 otherwise. The function should have a time complexity of O(log n), where n is the length of the array. The array may contain duplicate elements.
"""

def search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1