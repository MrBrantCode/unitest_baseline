"""
QUESTION:
Create a function named `row_sums` that takes a 2D array of integers as input and returns a 1D array where each element is the sum of the positive integers in the corresponding row of the input array. The input array will have at least one row and each row will have at least one element. The function should ignore any non-positive numbers in the array.
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