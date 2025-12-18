"""
QUESTION:
Implement a function `binary_search(arr, target)` that finds the position of a given target number in a list of integers `arr` sorted in ascending order, without using any built-in search functions or libraries. The function should have a time complexity of O(log n). If the target number is found, return its index; otherwise, return -1.
"""

def binary_search(arr, target):
    start = 0
    end = len(arr) - 1

    while start <= end:
        mid = (start + end) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            end = mid - 1
        else:
            start = mid + 1

    return -1