"""
QUESTION:
Write a function `average_cumulative_sum` that takes a nested list of integers as input and returns the average of the cumulative sums of its subarrays. The function should calculate the cumulative sum for each subarray independently and then find the average of these sums. If the input list is empty, the function should return 0.
"""

def average_cumulative_sum(nested_arr):
    total = 0
    count = 0
    for arr in nested_arr:
        total += sum(arr)
        count += 1
    return total / count if count > 0 else 0