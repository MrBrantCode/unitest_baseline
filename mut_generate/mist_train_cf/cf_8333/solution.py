"""
QUESTION:
Create a function `sum_2d_array` that takes a 2D array `arr` as input and returns the sum of all numeric elements in the array. The function should handle the following cases: 
- If the input array is `None`, return 0.
- If the array is empty or has empty sub-arrays, return 0.
- If the array contains non-numeric values, ignore them and only sum the numeric values.
Implement the function using a single loop or recursion, and ensure it is efficient and readable.
"""

def sum_2d_array(arr):
    if arr is None:
        return 0

    rows = len(arr)
    if rows == 0:
        return 0

    cols = len(arr[0])
    if cols == 0:
        return 0

    return sum_2d_array_recursive(arr, rows, cols, 0, 0)


def sum_2d_array_recursive(arr, rows, cols, current_row, current_col):
    if current_row >= rows:
        return 0

    if current_col >= cols:
        return sum_2d_array_recursive(arr, rows, cols, current_row + 1, 0)

    if not isinstance(arr[current_row][current_col], (int, float)):
        return sum_2d_array_recursive(arr, rows, cols, current_row, current_col + 1)

    return arr[current_row][current_col] + sum_2d_array_recursive(arr, rows, cols, current_row, current_col + 1)