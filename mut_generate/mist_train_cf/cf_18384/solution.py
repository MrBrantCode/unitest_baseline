"""
QUESTION:
Write a function `max_difference(arr)` to find the maximum difference between a lower element and an upper element in the given array, where the lower element must come before the upper element. The function should have a time complexity of O(n) and a space complexity of O(1), and it should not use any built-in sorting functions or data structures.
"""

def max_difference(arr):
    if len(arr) < 2:
        return 0

    min_value = arr[0]
    max_value = arr[0]
    max_diff = 0

    for i in range(1, len(arr)):
        if arr[i] < min_value:
            min_value = arr[i]
        elif arr[i] > max_value:
            max_value = arr[i]

        diff = max_value - min_value
        if diff > max_diff:
            max_diff = diff

    return max_diff