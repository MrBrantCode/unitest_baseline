"""
QUESTION:
Write a function `max_subarray_sum` that takes an array of integers as input and returns the sub-array with the highest sum of contiguous elements and the sum of the elements within this identified sub-array. The function should be implemented using Kadane's algorithm and should be able to handle arrays containing both positive and negative integers. The function should return a tuple containing the sub-array and the sum of its elements.
"""

def max_subarray_sum(arr):
    max_global = max_current = arr[0]
    start = end = 0
    temp = 0

    for i in range(1, len(arr)):
        max_current = max(arr[i], max_current + arr[i])

        # Update start index of max subarray
        if max_current == arr[i]:
            temp = i

        # Update global max and end index
        if max_global < max_current:
            max_global = max_current
            start = temp
            end = i

    return arr[start: end+1], max_global