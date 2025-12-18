"""
QUESTION:
Write two functions `bubble_sort(arr)` and `binary_search(arr, target)`. The `bubble_sort(arr)` function takes a list of integers as input and returns the sorted list in ascending order. The `binary_search(arr, target)` function takes a sorted list of integers and a target integer as input, and returns the index of the target in the list if found, otherwise returns -1. The list will contain at least one element and at most 10 elements. The elements in the list will be distinct integers.
"""

def entrance(arr, target):
    def bubble_sort(arr):
        n = len(arr)
        for i in range(n):
            for j in range(0, n-i-1):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]

    def binary_search(arr, target):
        low = 0
        high = len(arr) - 1

        while low <= high:
            mid = (low + high) // 2

            if arr[mid] == target:
                return mid
            elif arr[mid] < target:
                low = mid + 1
            else:
                high = mid - 1

        return -1

    bubble_sort(arr)
    return binary_search(arr, target)