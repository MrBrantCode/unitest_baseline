"""
QUESTION:
Create a function `binary_search` that takes two parameters: a sorted list of integers and a target integer to search for. The function should return the index of the target integer if found, and -1 otherwise.
"""

def binary_search(arr, target):
    start = 0
    end = len(arr) - 1

    while start <= end:
        mid = (start + end) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            start = mid + 1
        else:
            end = mid - 1

    return -1