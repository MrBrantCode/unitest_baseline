"""
QUESTION:
Design a function `max_subarray` that finds the maximum subarray in a given array of numbers. The function should return the starting index, ending index, and sum of the maximum subarray. The input array may contain floating point numbers and negative numbers. The function should have a time complexity of O(n log n) or better.
"""

def max_subarray(arr):
    max_ending_here = max_ending_so_far = arr[0]
    start = end = 0
    for i in range(1, len(arr)):
        if arr[i] > max_ending_here + arr[i]:
            max_ending_here = arr[i]
            start = i
        else:
            max_ending_here += arr[i]

        if max_ending_so_far < max_ending_here:
            max_ending_so_far = max_ending_here
            end = i

    return start, end, max_ending_so_far  