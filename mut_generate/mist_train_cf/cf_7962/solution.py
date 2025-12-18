"""
QUESTION:
Write a function `largest_sum_subarray` that takes a list of integers as input and returns the largest sum of any five consecutive integers in the list along with the indices of the starting and ending elements of the subarray with the largest sum.
"""

def largest_sum_subarray(arr):
    max_sum = float('-inf')
    max_start = 0
    max_end = 0

    for i in range(len(arr) - 4):
        curr_sum = sum(arr[i:i+5])
        if curr_sum > max_sum:
            max_sum = curr_sum
            max_start = i
            max_end = i+4

    return max_sum, [max_start, max_end]