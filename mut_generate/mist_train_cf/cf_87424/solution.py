"""
QUESTION:
Create a function named `sort_rows` that takes a two-dimensional array as input. The function should calculate the sum of each row and ignore any rows containing negative numbers. Then, it should return a new two-dimensional array where the rows are sorted in descending order based on their sums.
"""

def sort_rows(arr):
    # Calculate the sum of each row
    row_sums = [sum(row) for row in arr]

    # Create a list of tuples containing the row sums and their corresponding rows
    rows_with_sums = [(row_sum, row) for row_sum, row in zip(row_sums, arr) if not any(num < 0 for num in row)]

    # Sort the rows in descending order based on the row sums
    sorted_rows = sorted(rows_with_sums, key=lambda x: x[0], reverse=True)

    # Extract the sorted rows
    sorted_arr = [row for _, row in sorted_rows]

    return sorted_arr