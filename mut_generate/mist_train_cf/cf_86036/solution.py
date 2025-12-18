"""
QUESTION:
Create a function `sum_squares(arr)` that calculates the sum of squares of elements in a 2D array according to the formula x^2 + y^2, where x is the element and y is its respective index in the array.

Create another function `max_subarray_sum(arr, size)` that uses the first function to find the maximum sum of squares from all possible subarrays of a given size in the 2D array.

The functions should be as efficient as possible, considering both time and space complexity.
"""

def sum_squares(arr):
    """
    Calculate the sum of squares of elements in a 2D array according to the formula x^2 + y^2.

    Args:
        arr (list): A 2D array.

    Returns:
        int: The sum of squares of elements in the array.
    """
    sum_squares = 0
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            sum_squares += arr[i][j]**2 + i**2 + j**2
    return sum_squares


def max_subarray_sum(arr, size):
    """
    Find the maximum sum of squares from all possible subarrays of a given size in the 2D array.

    Args:
        arr (list): A 2D array.
        size (int): The size of the subarray.

    Returns:
        int: The maximum sum of squares from all possible subarrays.
    """
    n_row, n_col = len(arr), len(arr[0])
    max_sum = -1e9
    for i in range(n_row-size+1):
        for j in range(n_col-size+1):
            sub_arr = [row[j:j+size] for row in arr[i:i+size]]
            sum_sub_arr_squares = sum_squares(sub_arr)
            max_sum = max(max_sum, sum_sub_arr_squares)
    return max_sum