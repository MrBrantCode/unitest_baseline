"""
QUESTION:
Write a function called `max_subarray_sum` that takes a two-dimensional array `my_array` and two pairs of indices `start_row`, `end_row`, `start_col`, `end_col` as input. The function should return the maximum sum of any subarray within `my_array` that starts at position `(start_row, start_col)` and ends at position `(end_row, end_col)`. The array can have up to 1000 rows and 1000 columns, and the values in the array can range from -10^9 to 10^9. The specified indices for the subarray will always be valid.
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

    # Iterate through each pair of start and end rows and start and end columns
    for i in range(start_row, end_row+1):
        for j in range(start_col, end_col+1):
            # Calculate sum of subarray using prefix sum array
            subarray_sum = prefix_sum[i][j]
            if start_row > 0:
                subarray_sum -= prefix_sum[start_row-1][j]
            if start_col > 0:
                subarray_sum -= prefix_sum[i][start_col-1]
            if start_row > 0 and start_col > 0:
                subarray_sum += prefix_sum[start_row-1][start_col-1]

            # Update maximum sum
            max_sum = max(max_sum, subarray_sum)

    # Return maximum sum
    return max_sum