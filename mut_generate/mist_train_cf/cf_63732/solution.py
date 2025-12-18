"""
QUESTION:
Implement a function `shifted_binary_search` that performs a modified binary search on a cyclically shifted sorted array of unique integers. The function should take two parameters: `array` (a list of integers) and `target` (the integer to be searched). It should return the index of the `target` if it's present in the `array`, otherwise return -1. The function should achieve a time complexity of O(log n).
"""

def shifted_binary_search(array, target):
    left = 0
    right = len(array) - 1

    while left <= right:
        middle = left + (right - left) // 2
        if array[middle] == target:
            return middle
        elif array[left] <= array[middle]:
            if target >= array[left] and target < array[middle]:
                right = middle - 1
            else:
                left = middle + 1
        else:
            if target > array[middle] and target <= array[right]:
                left = middle + 1
            else:
                right = middle - 1

    return -1