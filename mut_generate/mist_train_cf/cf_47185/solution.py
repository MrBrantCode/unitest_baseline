"""
QUESTION:
Construct a function `mean_cumulative_sum` that accepts a 2D list of integers and returns the mean value of the cumulative sums of the subarrays. The function should calculate the cumulative sum for each subarray, store these sums, and then calculate the mean of these sums. The input list is expected to be non-empty and contain only non-empty subarrays of integers.
"""

def mean_cumulative_sum(arr):
    cumulative_sums = [sum(subarray) for subarray in arr]
    mean_value = sum(cumulative_sums) / len(cumulative_sums)
    return mean_value