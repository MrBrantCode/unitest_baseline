"""
QUESTION:
Given an array of integers, write a function `max_continuous_sum(arr)` that finds the maximum continuous sum that can be achieved by adding the numbers in the array, with the restriction that the maximum sum does not include any adjacent elements in the array. The function should have a time complexity of O(n).
"""

def max_continuous_sum(arr):
    if not arr:  # handle empty array
        return 0

    inclusive = arr[0]
    exclusive = 0

    for i in range(1, len(arr)):
        new_inclusive = exclusive + arr[i]
        exclusive = max(inclusive, exclusive)
        inclusive = new_inclusive

    return max(inclusive, exclusive)