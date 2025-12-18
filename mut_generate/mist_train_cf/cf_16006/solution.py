"""
QUESTION:
Write a function `search` that takes a sorted array `arr` and a target value `target` as parameters. The array may contain duplicate elements. The function should return the index of the target value in the array. If the target value is not found, the function should return -1. The time complexity of the function should be O(log n), where n is the length of the array.
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