"""
QUESTION:
Write a function called `longest_increasing_subsequence` that takes a list of integers as input and returns a tuple containing the starting and ending indices of the longest contiguous increasing subsequence in the list. The function should assume that the input list contains at least one element.
"""

def longest_increasing_subsequence(arr):
    n = len(arr)
    start = 0
    end = 0
    max_length = 0
    max_start = 0
    max_end = 0
    for i in range(1, n):
        if arr[i] > arr[i - 1]:
            end = i
        else:
            if end - start > max_length:
                max_length = end - start
                max_start = start
                max_end = end
            start = i
    if end - start > max_length:
        max_length = end - start
        max_start = start
        max_end = end
    return (max_start, max_end)