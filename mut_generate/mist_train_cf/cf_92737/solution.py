"""
QUESTION:
Implement a function `merge_sort(arr)` that takes a list of numbers as input and returns the list sorted in descending order. The function should have a time complexity of O(nlogn).
"""

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    result = []
    while left and right:
        if left[0] >= right[0]:
            result.append(left[0])
            left = left[1:]
        else:
            result.append(right[0])
            right = right[1:]

    result += left
    result += right

    return result