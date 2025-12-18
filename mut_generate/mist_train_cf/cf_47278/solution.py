"""
QUESTION:
Write a function `max_sum_subsequence(arr)` that takes an array of integers as input and returns the maximum sum of a subsequence within the array. The function should have a time complexity of O(n), where n is the length of the input array.
"""

def max_sum_subsequence(arr):
    max_so_far = float("-inf")
    max_ending_here = 0

    for i in range(len(arr)):
        max_ending_here += arr[i]
        if max_so_far < max_ending_here:
            max_so_far = max_ending_here

        if max_ending_here < 0:
            max_ending_here = 0

    return max_so_far