"""
QUESTION:
Write a function named `column_wise_sum` that takes a 2D array of integers as input and returns a list containing the column-wise sum of the array. The input array has n rows and m columns, where 1 <= n, m <= 10^6, and the elements are integers between -10^6 and 10^6. Do not use any built-in functions or libraries to calculate the column-wise sum, and ensure the function is optimized for large input arrays.
"""

def column_wise_sum(arr):
    rows = len(arr)
    cols = len(arr[0])

    # Initialize an empty list to store the column-wise sums
    sums = [0] * cols

    # Iterate through each column
    for j in range(cols):
        # Iterate through each row
        for i in range(rows):
            # Add the element at the current row and column to the sum
            sums[j] += arr[i][j]

    return sums