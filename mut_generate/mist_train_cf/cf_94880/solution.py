"""
QUESTION:
Create a function named `row_sums` that takes a 2D array of integers as input. The function should return a 1D array containing the sum of positive integers in each row of the input array, ignoring any negative numbers. The input array is guaranteed to have at least one row and each row will have at least one element.
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