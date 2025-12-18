"""
QUESTION:
Create a function named `sort_rows` that takes a 2D array as input and returns a new 2D array with rows sorted in descending order based on their sum. The function should ignore any rows that contain negative numbers. The function should not modify the original array.
"""

def sort_rows(arr):
    """
    Sorts the rows of a 2D array in descending order based on their sums, 
    ignoring any rows that contain negative numbers.

    Args:
        arr (list of lists): The input 2D array.

    Returns:
        list of lists: A new 2D array with rows sorted in descending order.
    """
    # Calculate the sum of each row and ignore rows containing negative numbers
    row_sums = [sum(row) for row in arr if all(num >= 0 for num in row)]

    # Sort the rows in descending order based on their sums
    sorted_arr = [x for _, x in sorted(zip(row_sums, [row for row in arr if all(num >= 0 for num in row)]), reverse=True)]
    return sorted_arr