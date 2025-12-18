"""
QUESTION:
Write a function `mean_cumulative_sum` that takes a 2D array of integers as input, calculates the cumulative sum of each subarray, and returns the arithmetic mean of these cumulative sums. The input array is a list of lists where each sublist contains integers. The function should return the mean as a floating point number.
"""

def mean_cumulative_sum(arr):
    cumulative_sums = [sum(subarray) for subarray in arr]
    return sum(cumulative_sums) / len(cumulative_sums)