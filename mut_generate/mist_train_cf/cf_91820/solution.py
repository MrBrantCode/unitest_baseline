"""
QUESTION:
Write a function `max_difference` to find the maximum difference between a lower element and an upper element in an array of integers. The lower element must come before the upper element in the array. The function must have a time complexity of O(n) and a space complexity of O(1), where n is the number of elements in the array.
"""

def max_difference(arr):
    if len(arr) < 2:
        return 0

    min_val = arr[0]
    max_diff = 0

    for i in range(1, len(arr)):
        if arr[i] < min_val:
            min_val = arr[i]
        else:
            diff = arr[i] - min_val
            if diff > max_diff:
                max_diff = diff

    return max_diff