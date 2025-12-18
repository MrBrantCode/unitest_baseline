"""
QUESTION:
Write a function max_subarray_sum that takes a two-dimensional array my_array and four integer parameters start_row, end_row, start_col, end_col as input. The function should return the maximum sum of any subarray within my_array that starts at row start_row and column start_col and ends at row end_row and column end_col.

Constraints: The array can have up to 1000 rows and 1000 columns. The values in the array can range from -10^9 to 10^9. The specified indices for the subarray will always be valid.
"""

def max_subarray_sum(my_array, start_row, end_row, start_col, end_col):
    rows = len(my_array)
    cols = len(my_array[0])

    # Initialize prefix sum array
    prefix_sum = [[0] * cols for _ in range(rows)]

    # Compute prefix sum array
    for i in range(rows):
        for j in range(cols):
            prefix_sum[i][j] = my_array[i][j]
            if i > 0:
                prefix_sum[i][j] += prefix_sum[i-1][j]
            if j > 0:
                prefix_sum[i][j] += prefix_sum[i][j-1]
            if i > 0 and j > 0:
                prefix_sum[i][j] -= prefix_sum[i-1][j-1]

    # Initialize maximum sum
    max_sum = float('-inf')

    # Calculate sum of subarray using prefix sum array
    subarray_sum = prefix_sum[end_row][end_col]
    if start_row > 0:
        subarray_sum -= prefix_sum[start_row-1][end_col]
    if start_col > 0:
        subarray_sum -= prefix_sum[end_row][start_col-1]
    if start_row > 0 and start_col > 0:
        subarray_sum += prefix_sum[start_row-1][start_col-1]

    # Update maximum sum
    max_sum = max(max_sum, subarray_sum)

    # Return maximum sum
    return max_sum