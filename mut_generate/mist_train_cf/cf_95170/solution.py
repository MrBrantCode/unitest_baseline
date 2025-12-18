"""
QUESTION:
Write a function `max_difference` that takes an array of integers as input and returns the maximum difference between a lower element and an upper element, where the lower element must come before the upper element in the array. The function should have a time complexity of O(n) and a space complexity of O(1), and should not use any built-in sorting functions or data structures.
"""

def max_difference(arr):
    if len(arr) < 2:
        return 0

    min_value = arr[0]
    max_diff = 0

    for i in range(1, len(arr)):
        if arr[i] < min_value:
            min_value = arr[i]
        else:
            diff = arr[i] - min_value
            if diff > max_diff:
                max_diff = diff

    return max_diff