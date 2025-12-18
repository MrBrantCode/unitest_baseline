"""
QUESTION:
Write a function called `find_max_row_sum` that takes a 2D array as input and returns a tuple containing the row with the maximum sum and a list of sums of every row. The function should be able to handle arrays with negative numbers and arrays where all sums are negative.
"""

def find_max_row_sum(arr):
    max_sum = float('-inf')
    max_row = None
    row_sums = []

    for i in range(len(arr)):
        row_sum = sum(arr[i])
        row_sums.append(row_sum)

        if row_sum > max_sum:
            max_sum = row_sum
            max_row = arr[i]
            
    return max_row, row_sums