"""
QUESTION:
Write a function `array_interval` that computes the greatest overall interval between the maximum element and the minimum element in a given 2D array. The function should also return the positions of the maximum and minimum elements in terms of array and sub-array indices. The function must iterate through all sub-arrays to find the overall maximum and minimum elements, not just the maximum and minimum within individual sub-arrays.
"""

def array_interval(arr):
    max_val = float('-inf')
    min_val = float('inf')
    max_pos = []
    min_pos = []

    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] > max_val:
                max_val = arr[i][j]
                max_pos = [i, j]
            if arr[i][j] < min_val:
                min_val = arr[i][j]
                min_pos = [i, j]

    interval = max_val - min_val
    return interval, max_pos, min_pos