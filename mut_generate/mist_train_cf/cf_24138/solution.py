"""
QUESTION:
Write a function `max_sum(arr)` that takes a two-dimensional array of integers as input and returns the maximum sum of numbers that can be found by tracing a path from the top-left to the bottom-right corner of the array. The path can only move either right or down at any point.
"""

def max_sum(arr):
    result = [[None] * len(arr[0]) for _ in range(len(arr))]
    result[0][0] = arr[0][0]
    for i in range(1, len(arr[0])):
        result[0][i] = arr[0][i] + result[0][i - 1]
    for i in range(1, len(arr)):
        result[i][0] = arr[i][0] + result[i - 1][0]
    for i in range(1, len(arr)):
        for j in range(1, len(arr[0])):
            result[i][j] = max(result[i - 1][j], result[i][j - 1]) + arr[i][j]
    return result[- 1][- 1]