"""
QUESTION:
Create a function named binary_search that takes two parameters: a sorted list of integers (arr) and a target integer (target). The function should return the index of the target in the list if it exists, otherwise return 'Not Found'. The input list will be sorted in ascending order, and the function should use a binary search algorithm to achieve this.
"""

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return "Not Found"