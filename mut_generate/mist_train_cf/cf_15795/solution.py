"""
QUESTION:
Implement a function called `binary_search` that takes a sorted array `arr` and a target value `target` as parameters, and returns `True` if the target value exists in the array and `False` otherwise. The array is sorted in ascending order and may contain duplicate elements, with a maximum length of 10^6. The function should have a time complexity of O(log n) and space complexity of O(1).
"""

def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return True
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return False