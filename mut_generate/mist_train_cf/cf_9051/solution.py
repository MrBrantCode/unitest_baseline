"""
QUESTION:
Create a function named binary_search that checks if a specific integer target is present in a sorted list of integers. The function should return the index of the target if it exists in the list and -1 otherwise. The list is sorted in ascending order and the function must have a time complexity of O(log n), where n is the length of the list. The function should take two parameters: arr (the sorted list of integers) and target (the target integer).
"""

def binary_search(arr, target):
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