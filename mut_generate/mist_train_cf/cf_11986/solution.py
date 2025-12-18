"""
QUESTION:
Write a function `sum_of_2d_array` that takes a 2-D array as input and returns the sum of its elements. The array can be empty or contain non-integer elements, and rows can have different lengths. If the input is invalid, the function should return an error message. The function should handle these invalid cases: the input is not a 2-D array, rows have different lengths, or the array contains non-integer elements.
"""

def sum_of_2d_array(arr):
    """
    This function calculates the sum of elements in a 2-D array.

    Args:
        arr (list of lists): A 2-D array of integers.

    Returns:
        int: The sum of elements in the array if the array is valid.
        str: An error message if the array is invalid.
    """
    if not arr or any([not isinstance(row, list) for row in arr]):
        return "Invalid input: array should be a non-empty 2-D array."

    row_lengths = set([len(row) for row in arr])
    if len(row_lengths) > 1:
        return "Invalid input: rows of different lengths."

    total_sum = 0
    for row in arr:
        for elem in row:
            if not isinstance(elem, int):
                return "Invalid input: array should only contain integers."
            total_sum += elem

    return total_sum