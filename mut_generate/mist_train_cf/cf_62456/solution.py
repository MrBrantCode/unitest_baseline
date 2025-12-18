"""
QUESTION:
Write a function `calculate_sums` that takes a 2D array as input and returns the total sum, row-wise sums, column-wise sums, primary diagonal sum, and secondary diagonal sum. The 2D array is a square matrix (i.e., the number of rows equals the number of columns).
"""

def calculate_sums(arr):
    """
    Calculate total sum, row-wise sums, column-wise sums, primary diagonal sum, and secondary diagonal sum of a 2D array.

    Args:
    arr (list): A 2D array (square matrix).

    Returns:
    tuple: A tuple containing total sum, row-wise sums, column-wise sums, primary diagonal sum, and secondary diagonal sum.
    """

    # Initialize sums at 0
    total_sum = 0
    rows_sum = [0] * len(arr)
    columns_sum = [0] * len(arr[0])
    primary_diagonal_sum = 0
    secondary_diagonal_sum = 0

    # Calculate sums
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            total_sum += arr[i][j]
            rows_sum[i] += arr[i][j]
            columns_sum[j] += arr[i][j]
            if i == j:
                primary_diagonal_sum += arr[i][j]
            if i + j == len(arr) - 1:
                secondary_diagonal_sum += arr[i][j]

    # Return the results
    return total_sum, rows_sum, columns_sum, primary_diagonal_sum, secondary_diagonal_sum