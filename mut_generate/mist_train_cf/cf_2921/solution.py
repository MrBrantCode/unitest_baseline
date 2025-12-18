"""
QUESTION:
Create a function named `row_sums` that takes a 2D array of integers as input and returns an array containing the sums of each row, ignoring any negative numbers and treating empty subarrays as having a sum of 0.
"""

def row_sums(arr):
    sums = []
    for row in arr:
        row_sum = 0
        for num in row:
            if num > 0:
                row_sum += num
        sums.append(row_sum)
    return sums