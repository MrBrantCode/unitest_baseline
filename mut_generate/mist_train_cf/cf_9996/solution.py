"""
QUESTION:
Write a function `find_max_difference_pair(arr)` that takes an array of integers as input and returns a pair of elements with the greatest difference, where the larger element is located at an index greater than the smaller element. If multiple pairs have the same maximum difference, return the pair with the smallest index of the smaller element.
"""

def find_max_difference_pair(arr):
    max_diff = float('-inf')
    pair = None
    left = 0
    right = len(arr) - 1

    while left < right:
        diff = arr[right] - arr[left]

        if diff > max_diff:
            max_diff = diff
            pair = (arr[left], arr[right])

        left += 1
        while left < right and arr[left] == arr[left - 1]:
            left += 1

        right -= 1
        while left < right and arr[right] == arr[right + 1]:
            right -= 1

    return pair