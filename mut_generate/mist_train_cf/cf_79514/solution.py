"""
QUESTION:
Write a function `min_consecutive_elements(arr, target)` that takes a one-dimensional numerical array `arr` and a numeric target `target` as input. The function should return the least number of consecutive elements within the array that sum up to exactly `target`. If no combination adds up to `target`, return 0.
"""

def min_consecutive_elements(arr, target):
    min_len = float("inf")
    left = 0
    for right in range(len(arr)):
        while sum(arr[left:right+1]) >= target:
            min_len = min(min_len, right - left + 1)
            left += 1
    return min_len if min_len != float("inf") else 0