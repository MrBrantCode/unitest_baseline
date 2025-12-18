"""
QUESTION:
Write a function `max_continuous_sum` that takes an array of integers as input and returns the maximum continuous sum that can be achieved by adding the numbers in the array without including any adjacent elements. Assume that the input array is not empty and contains only integers.
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