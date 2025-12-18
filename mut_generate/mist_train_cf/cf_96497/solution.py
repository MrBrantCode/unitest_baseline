"""
QUESTION:
Implement the function `binary_search_closest(arr, val)` to find the closest number to a given value `val` in a sorted array `arr`. If `val` is present in `arr`, return it as the closest number. If there are two numbers equally close to `val`, return the larger number.
"""

def binary_search_closest(arr, val):
    left = 0
    right = len(arr) - 1
    closest = float('inf')
    closest_num = None

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == val:
            return arr[mid]

        diff = abs(arr[mid] - val)

        if diff < closest:
            closest = diff
            closest_num = arr[mid]
        elif diff == closest and arr[mid] > closest_num:
            closest_num = arr[mid]

        if arr[mid] < val:
            left = mid + 1
        else:
            right = mid - 1

    return closest_num