"""
QUESTION:
Create a function named `max_subarray_sum` that takes a list of integers `arr` as input and returns the maximum sum that can be obtained by selecting a contiguous subarray from the input list.
"""

def max_subarray_sum(arr):
    max_sum = arr[0]
    current_sum = arr[0]

    for num in arr[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)

    return max_sum